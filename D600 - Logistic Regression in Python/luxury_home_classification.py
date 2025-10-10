### C2 ###

# import libraries and data
import pandas as pd
data = pd.read_csv("D600 Task 2 Dataset 1 Housing Information.csv")

# define dataframes
continuous = ['Price', 'SquareFootage', 'NumBathrooms', 'NumBedrooms', 'BackyardSpace', 'CrimeRate',
              'SchoolRating', 'AgeOfHome', 'DistanceToCityCenter', 'EmploymentRate', 'PropertyTaxRate',
              'RenovationQuality', 'LocalAmenities', 'TransportAccess', 'Floors', 'Windows']
categorical = ['Fireplace', 'HouseColor', 'Garage', 'IsLuxury']
continuous_df = data[continuous]
categorical_df = data[categorical]

# continuous data descriptive statistics
pd.set_option('display.max_columns', None)
print("Continuous variable descriptive statistics:\n", continuous_df.describe(include='all'),"\n",
    "Continuous variables modes:\n",continuous_df.mode().iloc[0],"\n")

# categorical variable descriptive statistics
print("Categorical variable descriptive statistics:\n")
for var in categorical_df:
    print(categorical_df[var].value_counts(), "\n",
          "Mode:", categorical_df[var].mode().iloc[0], "\n",
          "Unique Values:", categorical_df[var].nunique(), "\n")

### C3 ###

import matplotlib.pyplot as plt
import seaborn as sns

# univariate visualizations
# continuous variable histograms
for var in continuous_df:
    plt.figure(figsize=(8, 5))
    sns.histplot(data[var], bins=30)
    plt.title(f'Distribution of {var}')
    plt.xlabel(var)
    plt.ylabel('Count')
    plt.show()

# categorical variables count bar charts
for var in categorical_df:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=var, data=data)
    plt.title(f'Counts of {var}')
    plt.xlabel(var)
    plt.ylabel('Count')
    plt.show()

# bivariate visualizations
# continuous variables vs IsLuxury violin plots
for var in continuous_df:
    plt.figure(figsize=(8, 5))
    sns.violinplot(x='IsLuxury', y=var, data=data)
    plt.title(f'{var} by IsLuxury')
    plt.xlabel('IsLuxury')
    plt.ylabel(var)
    plt.show()

# categorical variables vs IsLuxury bar charts
for var in categorical_df:
    if var != 'IsLuxury':
        plt.figure(figsize=(8, 5))
        sns.countplot(x=var, hue='IsLuxury', data=data)
        plt.title(f'{var} by Luxury Status')
        plt.xlabel(var)
        plt.ylabel('Count')
        plt.legend(title='IsLuxury', labels=['Normal', 'Luxury'])
        plt.show()

### D1 ###

from sklearn.model_selection import train_test_split

variables = ['Price', 'SquareFootage', 'NumBathrooms', 'NumBedrooms', 'BackyardSpace', 'CrimeRate',
              'SchoolRating', 'AgeOfHome', 'DistanceToCityCenter', 'EmploymentRate', 'PropertyTaxRate',
              'RenovationQuality', 'LocalAmenities', 'TransportAccess', 'Floors', 'Windows',
              'Fireplace', 'HouseColor', 'Garage', 'IsLuxury']

variables_df = data[variables]

# one-hot encode HouseColor (is only categorical variable that is not binary)
variables_df_encoded = pd.get_dummies(variables_df, columns=['HouseColor'], drop_first=True)

# convert string columns to int
bool_cols = variables_df_encoded.select_dtypes(include=['bool']).columns
variables_df_encoded[bool_cols] = variables_df_encoded[bool_cols].astype(int)

for col in variables_df_encoded.columns:
    if variables_df_encoded[col].dtype == object:
        variables_df_encoded[col] = variables_df_encoded[col].str.strip().str.lower()
        variables_df_encoded.loc[:, col] = variables_df_encoded[col].map({'yes': 1, 'no': 0})


# split data 80 / 20
train_df, test_df = train_test_split(variables_df_encoded, test_size=0.2, random_state=42)

# make sure all data are numeric and print shape
train_df = train_df.apply(pd.to_numeric, errors='raise')
test_df  = test_df.apply(pd.to_numeric, errors='raise')
print("Train shape:", train_df.shape)
print("Test shape:", test_df.shape)

# csv export
train_df.to_csv('my_training_data.csv', index=False)
test_df.to_csv('my_testing_data.csv', index=False)


### D2 ###

import statsmodels.api as sm

y_train = train_df['IsLuxury']
X_train = train_df.drop(columns=['IsLuxury'])

# initial logistical regression
X_train = sm.add_constant(X_train, has_constant='add')
init_logit = sm.Logit(y_train, X_train).fit()
print(init_logit.summary(),'\n')
print("Initial AIC:", init_logit.aic)
print("Initial BIC:", init_logit.bic,'\n')

# backward elimination for optimization
def backward_elimination_logit(back_independents, back_dependent, significance_level=0.05):
    back_variables = [c for c in back_independents.columns if c != 'const']
    while True:
        x_w = sm.add_constant(back_independents[back_variables], has_constant='add')
        model = sm.Logit(back_dependent, x_w).fit(disp=False)

        pvals = model.pvalues.drop('const', errors='ignore')
        if pvals.empty:
            break

        max_pval = pvals.max()
        if max_pval > significance_level:
            worst = pvals.idxmax()
            print(f"Removing {worst} (p={max_pval:.4f})")
            back_variables.remove(worst)
        else:
            break
    return model, back_variables

optimized_logit_model, optimized_features = backward_elimination_logit(X_train, y_train)
print('\n',"Optimized features:", optimized_features,'\n')
print(optimized_logit_model.summary())
print("Optimized AIC:", optimized_logit_model.aic)
print("Optimized BIC:", optimized_logit_model.bic)

### D3 ###

from sklearn.metrics import confusion_matrix, accuracy_score

# predict probabilities for training set
y_train_pred_prob = optimized_logit_model.predict(sm.add_constant(X_train[optimized_features]))
y_train_pred_class = (y_train_pred_prob >= 0.5).astype(int)

# confusion matrix and accuracy
cm_train = confusion_matrix(y_train, y_train_pred_class)
train_accuracy = accuracy_score(y_train, y_train_pred_class)
print("\nConfusion Matrix (Training Set):\n", cm_train)
print(f"Training Accuracy: {train_accuracy:.4f}\n")

### D4 ###

# testing variables and predictions
X_test_opt = sm.add_constant(test_df[optimized_features], has_constant='add')
y_test = test_df['IsLuxury']
y_test_pred_prob = optimized_logit_model.predict(X_test_opt)
y_test_pred_class = (y_test_pred_prob >= 0.5).astype(int)

# testing confusion matrix and accuracy
test_conf_matrix = confusion_matrix(y_test, y_test_pred_class)
test_accuracy = accuracy_score(y_test, y_test_pred_class)
print("Confusion Matrix (Test Set):\n", test_conf_matrix)
print(f"Test Accuracy: {test_accuracy:.4f}")



import pandas as pd
import numpy as np
data = pd.read_csv("D600 Task 1 Dataset 1 Housing Information.csv")

### C2 ###

# add AverageRoomSize and BedBathRatio columns
data['AverageRoomSize'] = data['SquareFootage'] / (data['NumBathrooms'] + data['NumBedrooms'])
data['BedBathRatio'] = data['NumBedrooms'] / data['NumBathrooms'].replace(0, np.nan)

# define dataframes
continuous = ['Price', 'SquareFootage', 'NumBathrooms', 'NumBedrooms', 'RenovationQuality', 'Floors',
              'Windows', 'AverageRoomSize', 'BedBathRatio']
categorical = ['Fireplace', 'HouseColor', 'Garage', 'IsLuxury']
continuous_df = data[continuous]
categorical_df = data[categorical]

# continuous data descriptive statistics
pd.set_option('display.max_columns', None)
print("Continuous variable descriptive statistics:\n", continuous_df.describe(include='all'),"\n",
    "Continuous variables modes:\n",continuous_df.mode().iloc[0],"\n")

#categorical variable descriptive statistics
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
# continuous variables vs price scatterplots
for var in continuous_df:
    if var != 'Price':
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=var, y='Price', data=data)
        plt.title(f'Price vs. {var}')
        plt.xlabel(var)
        plt.ylabel('Price')
        plt.show()

# categorical variables vs price violin plots
for var in categorical_df:
    plt.figure(figsize=(8, 5))
    sns.violinplot(x=var, y='Price', data=data)
    plt.title(f'Price by {var}')
    plt.xlabel(var)
    plt.ylabel('Price')
    plt.show()


### D1 ###

from sklearn.model_selection import train_test_split

variables = ['Price', 'SquareFootage', 'NumBathrooms', 'NumBedrooms', 'RenovationQuality',
             'Fireplace', 'HouseColor', 'Garage', 'Floors', 'Windows', 'IsLuxury',
             'AverageRoomSize', 'BedBathRatio']

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

print("Train shape:", train_df.shape)
print("Test shape:", test_df.shape)

# csv export
train_df.to_csv('my_training_data.csv', index=False)
test_df.to_csv('my_testing_data.csv', index=False)


### D2 - Model training and optimization ###

import statsmodels.api as sm
train_df = pd.read_csv('my_training_data.csv')

# define model
dependent = train_df['Price']
independents = train_df.drop(columns=['Price'])
independents = sm.add_constant(independents)
full_model = sm.OLS(dependent, independents).fit()
print(full_model.summary())

# Backward elimination
def backward_elimination(back_independents, back_dependent, significance_level=0.05):
    back_variables = list(back_independents.columns)
    while True:
        back_independents_with_const = sm.add_constant(back_independents[back_variables], has_constant='add')
        model = sm.OLS(back_dependent, back_independents_with_const).fit()
        pvalues = model.pvalues.drop('const')
        max_pval = pvalues.max()
        if max_pval > significance_level:
            worst_feature = pvalues.idxmax()
            print(f"Removing {worst_feature} (p={max_pval:.4f})")
            back_variables.remove(worst_feature)

        else:
            break
    return model

optimized_model = backward_elimination(independents.drop(columns=['const'], errors='ignore'), dependent)
print(optimized_model.summary())

### D3 - MSE for optimized model ###

from sklearn.metrics import mean_squared_error

optimized_features = optimized_model.model.exog_names[1:]
X_train_opt = sm.add_constant(train_df[optimized_features])
Y_train_pred = optimized_model.predict(X_train_opt)
train_mse = mean_squared_error(train_df['Price'], Y_train_pred)
print(f"\nTraining Mean Squared Error (MSE): {train_mse:.2f}")


### D4 - MSE and Running Prediction on Test Data ###

test_df = pd.read_csv('my_testing_data.csv')

X_test_opt = sm.add_constant(test_df[optimized_features])
Y_test_pred = optimized_model.predict(X_test_opt)
test_mse = mean_squared_error(test_df['Price'], Y_test_pred)
print(f"\nTesting Mean Squared Error (MSE): {test_mse:.2f}")
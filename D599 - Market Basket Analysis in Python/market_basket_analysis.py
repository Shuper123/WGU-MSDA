### Part Zero - Load Data and Libraries ###

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv("Megastore_Dataset_Task_3 3.csv")


### Part One - Market Basket analysis on purchases ###

# true/false basket items
basket = pd.crosstab(df['OrderID'], df['ProductName'])
basket = basket.map(lambda x: True if x > 0 else False)

# apriori market basket analysis
frequent_itemsets = apriori(basket, min_support=0.05, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# prevent truncation
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# top three rules and csv export
top_rules = rules.sort_values(by='lift', ascending=False).head(3)
top_output = top_rules[['antecedents','consequents','support','confidence','lift']]
print("\n--- Analysis of product purchases only ---\nTop 3 Rules by Lift:")
print(top_output)

basket.to_csv("product_details_only.csv", index=False)


### Part Two - Include categorical variables in analysis ###

# one-hot encoded categorical dataframe and merge with product-only dataframe
categorical_vars = ['Region', 'Segment', 'ExpeditedShipping', 'DiscountApplied', 'CustomerOrderSatisfaction', 'OrderPriority']
df_categorical = pd.get_dummies(df[['OrderID'] + categorical_vars], columns=categorical_vars)
df_categorical = df_categorical.groupby('OrderID').max()
full_basket = pd.merge(basket, df_categorical, left_index=True, right_index=True)

# apriori analysis
frequent_itemsets_complete = apriori(full_basket, min_support=0.05, use_colnames=True)
rules_complete = association_rules(frequent_itemsets_complete, metric="lift", min_threshold=1)

# print top three rules and csv export
top_rules_complete = rules_complete.sort_values(by='lift', ascending=False).head(3)
top_output_complete = top_rules_complete[['antecedents','consequents','support','confidence','lift']]
print("\n--- Analysis with products and categorical variables ---\nTop 3 Rules by Lift:")
print(top_output_complete)
full_basket.to_csv("full_transaction_details.csv", index=False)


### Part Three - Only analyze categorical variables ###

# apriori analysis
frequent_itemsets_cat = apriori(df_categorical, min_support=0.05, use_colnames=True)
rules_cat = association_rules(frequent_itemsets_cat, metric="lift", min_threshold=1)
output_rules_cat = rules_cat[['antecedents','consequents','support','confidence','lift']]

# print top three rules and export csv
top_rules_cat = rules_cat.sort_values(by='lift', ascending=False).head(3)
top_output_cat = top_rules_cat[['antecedents','consequents','support','confidence','lift']]
print("\n--- Analysis of categorical variables only ---\nTop 3 Rules by Lift:")
print(top_output_cat)
df_categorical.to_csv("categorical_only.csv", index=False)
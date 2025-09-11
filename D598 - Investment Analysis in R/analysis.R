########## Load packages for varying functions in program ##########

# install readxl, if needed, in order to read excel file, and load library
if (!require("readxl")) install.packages("readxl")
library(readxl)

# install dplyr, if needed, for functions duplicate(), group_by()
if (!require("dplyr")) install.packages("dplyr")
library(dplyr)

# install janitor, if needed, for clean data importing
if (!require("janitor")) install.packages("janitor")
library(janitor)



########## Import data from “D598 Data Set” file into new data frame ##########

# load file into "initial" data frame
initial = read_excel("D598 Data Set.xlsx")                                                                            



########## Identify and remove any duplicate data points ##########

# count number of duplicate data points
duplicate_count = nrow(initial) - nrow(distinct(initial))

# communicate if duplicates are present and remove duplicates if they are present
if (duplicate_count == 0)
    {cat("This file does not have duplicate data points!", "\n")
    } else initial = {distinct(initial) 
         cat(duplicate_count, " duplicate data points were removed from this file!", "\n")
    }

# replace column names with "_" for easy data analysis
initial = clean_names(initial)
    
#visualize the cleaned initial data
View(initial)



######### In a new data frame, group data by state and perform descriptive statistics analysis ##########

# group data by state in new data frame
state_analysis = data.frame(group_by(initial, business_state))
    
# find mean, median, min, max for all numeric values in data
state_analysis = data.frame(summarize(group_by(state_analysis, business_state), across(where(is.numeric),list(
      mean   = ~mean(.x, na.rm = TRUE),
      median = ~median(.x, na.rm = TRUE),
      min    = ~min(.x, na.rm = TRUE),
      max    = ~max(.x, na.rm = TRUE)))))
      
# visualize the state analysis
View(state_analysis)



########## In a new data frame, identify all businesses with a negative debt-to-equity ratio ##########

# identify businesses with negative debt-to-equity ratio
negative_debt_to_equity = data.frame(filter(initial, debt_to_equity < 0))

# visualize the negative debt to equity list
View(negative_debt_to_equity)



########## Calculate the debt-to-income ratio for each business and add to original data##########

# calculate debt to income ratio as an update to the initial data frame
# if total_revenue is 0, the debt_to_income ratio will return an 'NA' value to avoid dividing by zero
updated_initial = mutate(initial, debt_to_income = if_else(total_revenue == 0, NA_real_, total_long_term_debt / total_revenue))



# visualize updated data
View(updated_initial)





########## Four business visualizations ##########

# install plotly, if needed, for data visualization
if (!require("plotly")) install.packages("plotly")
library(plotly)



##### median total_revenue per state bar graph #####

# define initial plot
median_revenue_plot = plot_ly(data = state_analysis, x = ~reorder(business_state, total_revenue_median), y = ~total_revenue_median, type = 'bar')

# make plot more pretty
median_revenue_plot = layout(median_revenue_plot, title = "Median Revenue by State", xaxis = list(title = "State"), yaxis = list(title = "Median Revenue"))

# display median_revenue_plot
median_revenue_plot



##### metrics for clients with negative debt-to-equity bar graph #####

# define shorted 'df' dataframe with desired metrics
# business_id interpreted as string to be plotted correctly
df = negative_debt_to_equity[, c("business_id", "total_long_term_debt", "total_equity", "total_liabilities", "total_revenue")]; df$business_id = as.character(df$business_id)

# set X-axis to show business ids
negative_debt_to_equity_plot = plot_ly(data = df, x = ~business_id)

# add total long term debt to each business id
negative_debt_to_equity_plot = add_trace(negative_debt_to_equity_plot, y = ~total_long_term_debt, type = "bar", name = "Long-Term Debt")

# add totol equity to each business id
negative_debt_to_equity_plot = add_trace(negative_debt_to_equity_plot, y = ~total_equity, type = "bar", name = "Equity")

# add total liabilities to each business id
negative_debt_to_equity_plot = add_trace(negative_debt_to_equity_plot, y = ~total_liabilities, type = "bar", name = "Liabilities")

# add total revenue to each business id
negative_debt_to_equity_plot = add_trace(negative_debt_to_equity_plot, y = ~total_revenue, type = "bar", name = "Revenue")

# adjust layout of final plot
negative_debt_to_equity_plot = layout(negative_debt_to_equity_plot, barmode = "group", title = "Metrics for Clients with Negative Debt-to-Equity", xaxis = list(title = "Business ID", tickangle = -45), yaxis = list(title = "Value"))

# display final plot
negative_debt_to_equity_plot



##### long term debt to total revenue relationship scatter plot #####

# define initial scatter plot parameters
scatter_plot = plot_ly(data = initial, x = ~total_long_term_debt, y = ~total_revenue, type = "scatter", mode = "markers")

# add a trend line
scatter_plot = add_trace(scatter_plot, x = ~total_long_term_debt, y = fitted(lm(total_revenue ~ total_long_term_debt, data = initial)), type = "scatter", mode = "lines", name = "Trend Line")

# adjust final layout
scatter_plot = layout(scatter_plot, title = "Revenue vs. Long-Term Debt", xaxis = list(title = "Long-Term Debt"), yaxis = list(title = "Revenue"))

# display final plot
scatter_plot



##### debt to equity histogram #####

# define initial histogram parameters
debt_to_equity_hist = plot_ly(data = initial, x = ~debt_to_equity, type = "histogram", nbinsx = 30)

# adjust final layout
debt_to_equity_hist = layout(debt_to_equity_hist, title = "Distribution of Debt-to-Equity Ratios", xaxis = list(title = "Debt-to-Equity Ratio"), yaxis = list(title = "Count"))

# display final plot
debt_to_equity_hist

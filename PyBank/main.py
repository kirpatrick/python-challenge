import os
import csv
import statistics

####################################################################
### References
### 11-Stu_UdemyZip
### netfliz.py
### comprehensions.py
### read_csv.py
####################################################################

# Read in 'budget_data.csv'
# Note: main.py is at the same level as the data folder,
# so reference same level in dir tree; '.'
budget_csv = os.path.join('.','data', 'budget_data.csv')

# Initialize variables
number_of_months = 0
profits = 0.00
losses = 0.00
total_profits = 0.00
initial_monthly_value = 0.00
current_change = 0.00
current_monthly_value = []

# Analyze

### Open and Read budget_csv
with open(budget_csv, newline='') as csvfile:

    #### Read budget_csv
    #### CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #### Read in header and skip in dataset
    csv_header = next(csvreader)

    #### Capture row count
    for row in csvreader:
        number_of_months = number_of_months + 1
        current_monthly_value.append(float(row[1]))

        if float(row[1]) < 0:
            losses = losses + float(row[1])
        else:
            profits = profits + float(row[1])

### End budget_csv read

### Print total number of months
print(number_of_months)

## The net total amount of "Profit/Losses" over the entire period
total_profits = profits + losses
print(total_profits)

## The average of the changes in "Profit/Losses" over the entire period
# print(average_change_over_time)

loop_count = 0

initial_monthly_value = current_monthly_value[0]
# print(initial_monthly_value)
# print(len(monthly_values))

monthly_change = []

for i in range(1,len(current_monthly_value)):
    monthly_change.append(current_monthly_value[i] - initial_monthly_value)
    initial_monthly_value = current_monthly_value[i]

print(statistics.mean(monthly_change))
# print(f"number of rows in average_change_over_time:  {loop_count}")
# print(initial_monthly_value)

## The greatest increase in profits (date and amount) over the entire period


## The greatest decrease in losses (date and amount) over the entire period


# Print analysis to terminal


# Save analysis to file
import os
import csv

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

# Analyze
## The total number of months included in the dataset
number_of_months = 0
profits = 0.00
losses = 0.00
profit_loss_percentage = 0.00

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

        if float(row[1]) < 0:
            losses = losses + float(row[1])
        else:
            profits = profits + float(row[1])

### End budget_csv read

### Print total number of months
print(number_of_months)

## The net total amount of "Profit/Losses" over the entire period
print(profits)
print(losses)
profit_loss_percentage = profits/losses
print(profit_loss_percentage)

total = profits + losses
print(total)

## The average of the changes in "Profit/Losses" over the entire period


## The greatest increase in profits (date and amount) over the entire period


## The greatest decrease in losses (date and amount) over the entire period


# Print analysis to terminal


# Save analysis to file
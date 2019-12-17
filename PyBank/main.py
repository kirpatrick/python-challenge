import os
import csv
import statistics

# Read in 'budget_data.csv'
budget_csv = os.path.join('.','data', 'budget_data.csv')

# Create dictionary to store budget data
myBudgetDataDictionary = {
    "month-year": [],
    "profit": []
}

### Open and Read budget_csv
with open(budget_csv, newline='') as csvfile:

    #### CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #### Read in header and skip in dataset
    csv_header = next(csvreader)

    #### Save budget data to myBudgetDataDictionary
    for row in csvreader:
        myBudgetDataDictionary["month-year"].append(row[0])
        myBudgetDataDictionary["profit"].append(float(row[1]))

### Print total number of months (records)
print(len(myBudgetDataDictionary["month-year"]))

## The net total amount of "Profit/Losses" over the entire period
print(round(sum(myBudgetDataDictionary["profit"])))

## The average of the changes in "Profit/Losses" over the entire period
### Store profits for the first recorded month
initial_monthly_value = myBudgetDataDictionary["profit"][0]

### Create dictionary to store changes in profit/loss
monthlyChangeDictionary = {
    "month-year": [],
    "profit": []
}

### iterate through all budget data in myBudgetDataDictionary
for i in range(1,len(myBudgetDataDictionary["profit"])):

    #### Store first month's comparison data into myBudgetDataDictionary.  E.g. currentMonth - previousMonth
    #### Capture month-year
    monthlyChangeDictionary["month-year"].append(myBudgetDataDictionary["month-year"][i])
    #### Capture change in USD
    monthlyChangeDictionary["profit"].append(myBudgetDataDictionary["profit"][i] - initial_monthly_value)

    #### Iterate the initial value for next comparison
    initial_monthly_value = myBudgetDataDictionary["profit"][i]

### Return the average monthly change
print(round(statistics.mean(monthlyChangeDictionary["profit"]),2))

## The greatest increase in profits (date and amount) over the entire period
### Given the index for max profit increase in monthlyChangeDictionary, return the month-year
print(monthlyChangeDictionary["month-year"][monthlyChangeDictionary["profit"].index(max(monthlyChangeDictionary["profit"]))])
### Return max profit increase USD
print(round(max(monthlyChangeDictionary["profit"])))

## The greatest decrease in losses (date and amount) over the entire period
### Given the index for max profit decrease in monthlyChangeDictionary, return the month-year
print(monthlyChangeDictionary["month-year"][monthlyChangeDictionary["profit"].index(min(monthlyChangeDictionary["profit"]))])
### Return max profit decrease USD
print(round(min(monthlyChangeDictionary["profit"])))

# Print analysis to terminal
## Need to format print statements

# Save analysis to file
output_file = os.path.join('.','data', 'output.csv')

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(
        [
            "Title",
            "Price",
            "Subscriber Count",
            "Number of Reviews", 
            "Course Length"
            ]
        )
import os
import csv
import statistics

# Read in 'budget_data.csv'
budget_csv = os.path.join('.','data', 'budget_data.csv')

# Create dictionary to store budget data
monthlyProfitDictionary = {
    "month-year": [],
    "profit": []
}

### Open budget_csv
with open(budget_csv, newline='') as csvfile:

    #### Specify csv delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #### Don't add header to new dataset
    csv_header = next(csvreader)

    #### Read budget_csv from csvreader into monthlyProfitDictionary
    for row in csvreader:
        monthlyProfitDictionary["month-year"].append(row[0])
        monthlyProfitDictionary["profit"].append(float(row[1]))

## The average of the changes in "Profit/Losses" over the entire period
### Store profits for the first recorded month
initial_monthly_value = monthlyProfitDictionary["profit"][0]

### Create dictionary to store changes in profit/loss
monthlyChangeDictionary = {
    "month-year": [],
    "profit": []
}

### iterate through all budget data in monthlyProfitDictionary
for i in range(1,len(monthlyProfitDictionary["profit"])):

    #### Store first month's comparison data into monthlyProfitDictionary.  E.g. currentMonth - previousMonth
    #### Capture month-year
    monthlyChangeDictionary["month-year"].append(monthlyProfitDictionary["month-year"][i])
    #### Capture change in USD
    monthlyChangeDictionary["profit"].append(monthlyProfitDictionary["profit"][i] - initial_monthly_value)

    #### Iterate the initial value for next comparison
    initial_monthly_value = monthlyProfitDictionary["profit"][i]

## Store profit change
profitChange = monthlyChangeDictionary["profit"]

## Store index for the Greatest Increase in Profits
# maxMonthlyChangeIndex = monthlyChangeDictionary["profit"].index(max(monthlyChangeDictionary["profit"]))
maxMonthlyChangeIndex = profitChange.index(max(profitChange))

## Store index for the Greatest Decrease in Profits
# minMonthlyChangeIndex = monthlyChangeDictionary["profit"].index(min(monthlyChangeDictionary["profit"]))
minMonthlyChangeIndex = profitChange.index(min(profitChange))

# Print analysis to terminal
print("Financial Analysis")
print("---------------------------------")
## Total number of months (records)
print("Total Months:  " + str(len(monthlyProfitDictionary["month-year"])))
## Total amount of "Profit/Losses" over the entire period
print("Total:  $" + str(round(sum(monthlyProfitDictionary["profit"]))))
## Average of the changes in "Profit/Losses" over the entire period
print("Average Change:  $" + str(round(statistics.mean(monthlyChangeDictionary["profit"]),2)))
## Greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits:  " + str(monthlyChangeDictionary["month-year"][maxMonthlyChangeIndex])+" ($" + str(round(max(monthlyChangeDictionary["profit"])))+")")
## Greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Profits:  " + str(monthlyChangeDictionary["month-year"][minMonthlyChangeIndex])+" ($" + str(round(min(monthlyChangeDictionary["profit"])))+")")

# Save analysis to file
output_file = os.path.join('.','data', 'output.txt')

with open(output_file, "w", newline="") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("---------------------------------\n")
    datafile.write("Total Months:  " + str(len(monthlyProfitDictionary["month-year"])) + "\n")
    datafile.write("Total:  $" + str(round(sum(monthlyProfitDictionary["profit"])))+"\n")
    datafile.write("Average Change:  $" + str(round(statistics.mean(monthlyChangeDictionary["profit"]),2))+"\n")
    datafile.write("Greatest Increase in Profits:  " + str(monthlyChangeDictionary["month-year"][maxMonthlyChangeIndex]))
    datafile.write(" ($" + str(round(max(monthlyChangeDictionary["profit"])))+")\n")
    datafile.write("Greatest Decrease in Profits:  " + str(monthlyChangeDictionary["month-year"][minMonthlyChangeIndex]))
    datafile.write(" ($" + str(round(min(monthlyChangeDictionary["profit"])))+")")
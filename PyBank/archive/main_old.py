import os
import csv
import statistics

# Create path to 'budget_data.csv'
budget_csv = os.path.join('.','data', 'budget_data.csv')

# Create dictionary to store budget data
monthlyProfitDictionary = {"month-year": [], "profit": []}

## Create monthlyProfitDictionary fields for readability
monthlyProfit = monthlyProfitDictionary["profit"]
monthlyProfitDate = monthlyProfitDictionary["month-year"]

### Open budget_csv
with open(budget_csv, newline='') as csvfile:

    #### Specify csv delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #### Don't add header to new dataset
    csv_header = next(csvreader)

    #### Read budget_csv from csvreader into monthlyProfitDictionary
    for row in csvreader:
        monthlyProfitDate.append(row[0])
        monthlyProfit.append(float(row[1]))

### Store profits for the first recorded month
initial_monthly_value = monthlyProfit[0]

### Create dictionary to store changes in profit/loss
monthlyChangeDictionary = {"month-year": [], "profit": []}

## Create monthlyChangeDictionary fields for readability
profitChange = monthlyChangeDictionary["profit"]
profitChangeDate = monthlyChangeDictionary["month-year"]

### iterate through all budget data in monthlyProfitDictionary
for i in range(1,len(monthlyProfit)):

    #### Store first month's comparison data into monthlyProfitDictionary.  E.g. currentMonth - previousMonth
    #### Capture month-year
    profitChangeDate.append(monthlyProfitDate[i])
    #### Capture change in USD
    profitChange.append(monthlyProfit[i] - initial_monthly_value)

    #### Iterate the initial value for next comparison
    initial_monthly_value = monthlyProfit[i]

## Store index for the Greatest Increase in Profits
maxMonthlyChangeIndex = profitChange.index(max(profitChange))

## Store index for the Greatest Decrease in Profits
minMonthlyChangeIndex = profitChange.index(min(profitChange))

# Print analysis to terminal
print("Financial Analysis")
print("---------------------------------")
## Total number of months (records)
print(f"Total Months:  {len(monthlyProfitDate)}")
## Total amount of "Profit/Losses" over the entire period
print(f"Total:  ${round(sum(monthlyProfit))}")
## Average of the changes in "Profit/Losses" over the entire period
print(f"Average Change:  ${round(statistics.mean(profitChange),2)}")
## Greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in Profits:  {profitChangeDate[maxMonthlyChangeIndex]} (${round(max(profitChange))})")
## Greatest decrease in losses (date and amount) over the entire period
print(f"Greatest Decrease in Profits:  {profitChangeDate[minMonthlyChangeIndex]} (${round(min(profitChange))})")

# Save analysis to file
output_file = os.path.join('.','data', 'output.txt')

with open(output_file, "w", newline="") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("---------------------------------\n")
    datafile.write(f"Total Months:  {len(monthlyProfitDate)} \n")
    datafile.write(f"Total:  ${round(sum(monthlyProfit))}\n")
    datafile.write(f"Average Change:  ${round(statistics.mean(profitChange),2)}\n")
    datafile.write(f"Greatest Increase in Profits:  {profitChangeDate[maxMonthlyChangeIndex]} (${round(max(profitChange))})\n")
    datafile.write(f"Greatest Decrease in Profits:  {profitChangeDate[minMonthlyChangeIndex]} (${round(min(profitChange))})")
import os
import csv
import statistics

monthlyProfitDictionary = {"month-year": [], "profit": []}
monthlyProfit = monthlyProfitDictionary["profit"]
monthlyProfitDate = monthlyProfitDictionary["month-year"]

# Read in budget_data and store in dictionary, exclude header
budget_csv = os.path.join('.','data', 'budget_data.csv')
with open(budget_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        monthlyProfitDate.append(row[0])
        monthlyProfit.append(float(row[1]))

monthlyChangeDictionary = {"month-year": [], "profit": []}
profitChange = monthlyChangeDictionary["profit"]
profitChangeDate = monthlyChangeDictionary["month-year"]

# Store month-to-month profit change in separate dictionary
initial_monthly_value = monthlyProfit[0]
for i in range(1,len(monthlyProfit)):
    profitChangeDate.append(monthlyProfitDate[i])
    profitChange.append(monthlyProfit[i] - initial_monthly_value)

    initial_monthly_value = monthlyProfit[i]

maxMonthlyChangeIndex = profitChange.index(max(profitChange))
minMonthlyChangeIndex = profitChange.index(min(profitChange))

# Print analysis to terminal
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months:  {len(monthlyProfitDate)}")
print(f"Total:  ${round(sum(monthlyProfit))}")
print(f"Average Change:  ${round(statistics.mean(profitChange),2)}")
print(f"Greatest Increase in Profits:  {profitChangeDate[maxMonthlyChangeIndex]} (${round(max(profitChange))})")
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
import os
import csv
import statistics

####################################################################
### References
### 11-Stu_UdemyZip
### netfliz.py
### comprehensions.py
### read_csv.py
### dictionaries.py
####################################################################

# Read in 'budget_data.csv'
# Note: main.py is at the same level as the data folder,
# so reference same level in dir tree; '.'
budget_csv = os.path.join('.','data', 'budget_data.csv')

# Initialize variables
initial_monthly_value = 0.00
current_monthly_value = []

# dictionary
myDictionary = {
    "month-year": [],
    "profit": []
}

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
        current_monthly_value.append(float(row[1]))

        myDictionary["month-year"].append(row[0])
        myDictionary["profit"].append(float(row[1]))

### Print total number of months
# print(len(current_monthly_value))
print(len(myDictionary["month-year"]))

## The net total amount of "Profit/Losses" over the entire period
# print(round(sum(current_monthly_value)))
print(round(sum(myDictionary["profit"])))

## The average of the changes in "Profit/Losses" over the entire period

# initial_monthly_value = current_monthly_value[0]
initial_monthly_value = myDictionary["profit"][0]

monthly_change = []

monthlyChangeDictionary = {
    "month-year": [],
    "profit": []
}

for i in range(1,len(myDictionary["profit"])):

    monthly_change.append(myDictionary["profit"][i] - initial_monthly_value)
    monthlyChangeDictionary["month-year"].append(myDictionary["month-year"][i])
    monthlyChangeDictionary["profit"].append(myDictionary["profit"][i] - initial_monthly_value)

    initial_monthly_value = myDictionary["profit"][i]

# print(round(statistics.mean(monthly_change),2))
print(round(statistics.mean(monthlyChangeDictionary["profit"]),2))

## The greatest increase in profits (date and amount) over the entire period
# print(round(max(monthly_change)))
print(round(max(monthlyChangeDictionary["profit"])))
# Return index for month-year of greatest decrease
print(monthlyChangeDictionary["profit"].index(max(monthlyChangeDictionary["profit"])))
print(monthlyChangeDictionary["month-year"][monthlyChangeDictionary["profit"].index(max(monthlyChangeDictionary["profit"]))])

## The greatest decrease in losses (date and amount) over the entire period
print(round(min(monthlyChangeDictionary["profit"])))
# Return index for month-year of greatest decrease
print(monthlyChangeDictionary["profit"].index(min(monthlyChangeDictionary["profit"])))
print(monthlyChangeDictionary["month-year"][monthlyChangeDictionary["profit"].index(min(monthlyChangeDictionary["profit"]))])

# Print analysis to terminal


# Save analysis to file
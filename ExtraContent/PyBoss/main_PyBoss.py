import os
import csv
import statistics

# need access to 'set' method to return unique candidate names
from itertools import chain

# Create dictionary to store poll data
employeeDataDictionary = {"EmpID": [], "Name": [], "DOB": [], "SSN": [], "State": []}
# Create field refs b/c that's a lot to type everytime!!!
emplDataEmplID = employeeDataDictionary["EmpID"]
emplDataName = employeeDataDictionary["Name"]
emplDataDOB = employeeDataDictionary["DOB"]
emplDataSSN = employeeDataDictionary["SSN"]
emplDataState = employeeDataDictionary["State"]
#################################################################################

# Read in election and store in dictionary, exclude header
employee_csv = os.path.join('.','data', 'employee_data.csv')
with open(employee_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        emplDataEmplID.append(row[0])
        emplDataName.append(row[1])
        emplDataDOB.append(row[2])
        emplDataSSN.append(row[3])
        emplDataState.append(row[4])
#################################################################################

# Test data read
print(emplDataEmplID[0])
print(emplDataName[0])
print(emplDataDOB[0])
print(emplDataSSN[0])
print(emplDataState[0])
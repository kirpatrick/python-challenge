import os
import csv
import statistics
from us_states import us_state_abbrev

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
# print(emplDataEmplID[0])
# print(emplDataName[0])
# print(emplDataDOB[0])
# print(emplDataSSN[0])
# print(emplDataState[0])
#################################################################################

# Create a disctionary to store the converted employee records
convertedEmplDataDictionary = {
    "convertedEmplID": [],
    "convertedEmplFirstName": [],
    "convertedEmplLastName": [],
    "convertedEmplDOB": [],
    "convertedEmplSSN": [],
    "convertedEmplState": [],
}
# Create field dictionary refs b/c that's a lot to type everytime!!!
newID = convertedEmplDataDictionary["convertedEmplID"]
newFirstName = convertedEmplDataDictionary["convertedEmplFirstName"]
newLastName = convertedEmplDataDictionary["convertedEmplLastName"]
newDOB = convertedEmplDataDictionary["convertedEmplDOB"]
newSSN = convertedEmplDataDictionary["convertedEmplSSN"]
newState = convertedEmplDataDictionary["convertedEmplState"]

# The Name column should be split into separate First Name and Last Name columns.
for i in range(0,len(emplDataEmplID)):
    fullName = emplDataName[i].split()
    newFirstName.append(fullName[0])
    newLastName.append(fullName[1])
#################################################################################

# The DOB data should be re-written into MM/DD/YYYY format.
# Currently YYYY-MM-DD.  Open in Notepad...NOT Excel!!!
for i in range(0,len(emplDataEmplID)):
    DOB = emplDataDOB[i].split("-")
    newDOB.append(f"{DOB[1]}/{DOB[2]}/{DOB[0]}")
#################################################################################


# The SSN data should be re-written such that the first five numbers are hidden from view.
for i in range(0,len(emplDataEmplID)):
    SSN = emplDataSSN[i].split("-")
    newSSN.append(str(f"***-**-{SSN[2]}"))
#################################################################################

# The State data should be re-written as simple two-letter abbreviations.
myStateDictionary = {"state": [],"abbreviation": []}

myState = myStateDictionary["state"]
myAbbreviation = myStateDictionary["abbreviation"]
for key, value in us_state_abbrev.items():
    myState.append(key)
    myAbbreviation.append(value)

for i in range(0,len(emplDataEmplID)):
    for j in range(0,len(myState)):
        if emplDataState[i] == myState[j]:
            newState.append(myAbbreviation[j])
            # print("Loop works!")
#################################################################################
# # Test
print(newFirstName[0])
print(newLastName[0])
print(newDOB[0])
print(newSSN[0])
# print(f'{us_state_abbrev["Alabama"]}')
# print(f'{us_state_abbrev.keys()}')
# print(f'{us_state_abbrev.items()}')
print(newState[0])
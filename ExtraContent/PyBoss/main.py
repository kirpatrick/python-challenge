import os
import csv
import statistics
# local import of state to stateAbbreviation lookup
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
    newID.append(emplDataEmplID[i])
#################################################################################

# The DOB data should be re-written into MM/DD/YYYY format.
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
# Create field dictionary refs b/c that's a lot to type everytime!!!
myState = myStateDictionary["state"]
myAbbreviation = myStateDictionary["abbreviation"]

# Save local state abbreviation to indexable reference dictionary
for key, value in us_state_abbrev.items():
    myState.append(key)
    myAbbreviation.append(value)

# Covert full state name to abbreviation
for i in range(0,len(emplDataEmplID)):
    for j in range(0,len(myState)):
        if emplDataState[i] == myState[j]:
            newState.append(myAbbreviation[j])
#################################################################################

# Save conversion to formated_employee_data.csv file
output_file = os.path.join('.','data', 'formated_employee_data.csv')
with open(output_file, 'w', newline="") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['EMP ID','First Name','Last Name','DOB','SSN','State'])

    for i in range(0,len(newID)):
        csvwriter.writerow([newID[i],newFirstName[i],newLastName[i],newDOB[i],newSSN[i],newState[i]])
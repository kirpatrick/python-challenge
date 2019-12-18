import os
import csv
import statistics

# Create dictionary to store poll data
electionDataDictionary = {"voter-id": [], "county": [], "candidate": []}
# Create field refs b/c that's a lot to type everytime!!!
electionDataVoterID = electionDataDictionary["voter-id"]
electionDataCounty = electionDataDictionary["county"]
electionDataCandidate = electionDataDictionary["candidate"]
#################################################################################

# Read in file
election_csv = os.path.join('.','data', 'election_data.csv')
with open(election_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        electionDataVoterID.append(row[0])
        electionDataCounty.append(row[0])
        electionDataCandidate.append(row[0])
#################################################################################

# Analyze
## The total number of votes cast


## A complete list of candidates who received votes


## The percentage of votes each candidate won


## The total number of votes each candidate won


## The winner of the election based on popular vote


# Print analysis to terminal


# Save analysis to file
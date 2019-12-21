import os
import csv
import statistics
from itertools import chain

# Create dictionary to store poll data
electionDataDictionary = {"voter-id": [], "county": [], "candidate": []}
# Create field refs b/c that's a lot to type everytime!!!
electionDataVoterID = electionDataDictionary["voter-id"]
electionDataCounty = electionDataDictionary["county"]
electionDataCandidate = electionDataDictionary["candidate"]
#################################################################################

# Read in election and store in dictionary, exclude header
election_csv = os.path.join('.','data', 'election_data.csv')
with open(election_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        electionDataVoterID.append(row[0])
        electionDataCounty.append(row[1])
        electionDataCandidate.append(row[2])
#################################################################################

# Test data read
# print(f"VoterID: {electionDataVoterID[0]}\n County: {electionDataCounty[1]}\n Election Candidate: {electionDataCandidate[1]}")
#################################################################################

# Analyze
## The total number of votes cast
print(f"Total Votes: {len(electionDataVoterID)}")
#################################################################################

# A complete list of candidates who received votes

# Create a dictionary to store number of votes recieved by each candidate
votesRecievedDictionary = {"county": [], "candidate": [], "voteCount": []}
# Create field refs b/c that's a lot to type everytime!!!
profitChange = votesRecievedDictionary["county"]
profitChangeDate = votesRecievedDictionary["candidate"]



for i in range(0,len(electionDataVoterID)):
#################################################################################    

# The percentage of votes each candidate won


#################################################################################

# The total number of votes each candidate won

#################################################################################

# The winner of the election based on popular vote

#################################################################################

# Print analysis to terminal

#################################################################################

# Save analysis to file

#################################################################################
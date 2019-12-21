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

# Get unique list of candidates
candidateList = set(electionDataCandidate)
print(candidateList)

# # Create a dictionary to store number of votes recieved by each candidate
# votesRecievedDictionary = {"candidate": [], "voteCount": []}
# # Create field refs b/c that's a lot to type everytime!!!
# candidate = votesRecievedDictionary["candidate"]
# voteCount = votesRecievedDictionary["voteCount"]

# # Initialize candidate
# existingCandidate = candidate.append(electionDataCandidate[0])
# # Tally each vote
# for i in range(0,len(electionDataVoterID)):
#     # check if existing candidate
#     if candidate[i] == existingCandidate:
#         voteCount[i] = voteCount[i] + 1
#     else:


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
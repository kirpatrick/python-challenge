import os
import csv
import statistics

# need access to 'set' method to return unique candidate names
from itertools import chain

# want to time script execution
import time

start_time = time.time()

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
totalVotes = len(electionDataVoterID)
print(f"Total Votes: {totalVotes}")
#################################################################################

# A complete list of candidates who received votes

# Get unique list of candidates
# candidateList = set(electionDataCandidate)
# print(candidateList)

# Create a dictionary to store number of votes recieved by each candidate
votesRecievedDictionary = {"candidate": [], "voteCount": []}

# Create field dictionary refs b/c that's a lot to type everytime!!!
candidate = votesRecievedDictionary["candidate"]
voteCount = votesRecievedDictionary["voteCount"]

# Initialize candidate list with unique candidates for tally
# candidate = list(sorted(set(electionDataCandidate)))

print(candidate)

# candidateOneTotal = sum(1 for i in electionDataDictionary if electionDataCandidate[i] == candidate[0])

# print(f"Candidate One got {candidateOneTotal} votes.")


# Initialize vote counts
voteCount = [0,0,0,0]

# print(candidate[0])
# print(len(candidate))
# candidate.append("Kirpatrick")
# # Make sure this works as expected
# print(candidate)
# print("")
# print(votesRecievedDictionary["candidate"])
# # Confirmed...changing candidate updated the dictionary

# Catch unknown candidate entries
# unknownCandidateIndex = 4

# # Tally each vote in election data
# for i in range(0,totalVotes):
#     # Check against the candidates list
#     for j in range(0,len(candidate)):
#         # Tally votes for known candidates
        
#         if electionDataCandidate[i] == candidate[j]:
#             voteCount[j] = voteCount[j] + 1
#         # Add unknown candidates if exist
#         else:
#             # Add the unknown candidate's name to the list
#             candidate.append(electionDataCandidate[i])
#             # Tally 1 vote for new candidate
#             voteCount.append(1)


# print("\nCandidate 0")
# print(candidate[0])
# print(voteCount[0])
# print("Candidate 1")
# print("\nCandidate 1")
# print(candidate[1])
# print(voteCount[1])
# print("\nCandidate 2")
# print(candidate[2])
# print(voteCount[2])
# print("\nCandidate 3")
# print(candidate[3])
# print(voteCount[3])

    
    # # Tally votes...
    # # For the 1st candidate
    # if electionDataCandidate[i] == candidate[0]:
    #     voteCount[0] = voteCount[0] + 1
    # # For the 2nd candidate
    # elif electionDataCandidate[i] == candidate[1]:
    #     voteCount[1] = voteCount[1] + 1
    # # For the 3rd candidate
    # elif electionDataCandidate[i] == candidate[2]:
    #     voteCount[2] = voteCount[2] + 1
    # # For the 4th candidate
    # elif electionDataCandidate[i] == candidate[3]:
    #     voteCount[3] = voteCount[3] + 1
    # # Not in the Original Candidate List
    # else:
    #     # Add the unknown candidate's name to the list
    #     candidate.append(candidate[i])
    #     # Tally a vote for this candidate
    #     voteCount.append(1)
    #     [unknownCandidateIndex] == candidate[3]:
    #     voteCount[3] = voteCount[3] + 1

# print(votesRecievedDictionary)
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

print("--- %s second runtime ---" % (time.time() - start_time))
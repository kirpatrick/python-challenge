import os
import csv
import statistics

# need access to 'set' method to return unique candidate names
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

# Begin Election Data Analysis

# The total number of votes cast
totalVotes = len(electionDataVoterID)
#################################################################################

# Create a dictionary to store number of votes recieved by each candidate
votesRecievedDictionary = {"candidate": [], "voteCount": []}
# Create field dictionary refs b/c that's a lot to type everytime!!!
candidate = votesRecievedDictionary["candidate"]
voteCount = votesRecievedDictionary["voteCount"]
#################################################################################

# Initialize candidate list with unique candidates for tally
candidate = list(sorted(set(electionDataCandidate)))
# Initialize vote counts
voteCount = [0,0,0,0]
#################################################################################

# Tally each vote in election data 
for i in range(0,totalVotes):
    # Tally votes...
    # For the 1st candidate
    if electionDataCandidate[i] == candidate[0]:
        voteCount[0] = voteCount[0] + 1
    # For the 2nd candidate
    elif electionDataCandidate[i] == candidate[1]:
        voteCount[1] = voteCount[1] + 1
    # For the 3rd candidate
    elif electionDataCandidate[i] == candidate[2]:
        voteCount[2] = voteCount[2] + 1
    # For the 4th candidate
    elif electionDataCandidate[i] == candidate[3]:
        voteCount[3] = voteCount[3] + 1
    # Not in the Original Candidate List
    else:
        # Add the unknown candidate's name to the list
        candidate.append(electionDataCandidate[i])
        # Tally a vote for this candidate
        voteCount.append(1)
#################################################################################

# Record the idex of highest number of votes
maxPopularVoteIndex = voteCount.index(max(voteCount))
#################################################################################

# Print Results to terminal
print("Election Results")
print("---------------------------------")

# The total number of votes cast
print(f"Total Votes:  {totalVotes}")
print("---------------------------------")
#################################################################################

# The percentage and total number of votes each candidate won
for i in range(0,len(candidate)):
    print(f"{candidate[i]}:  {format(float(voteCount[i]/totalVotes)*100, '.3f')}% ({voteCount[i]})")
print("---------------------------------")
#################################################################################

# The winner of the election based on popular vote
print(f"Winner:  {candidate[maxPopularVoteIndex]}")
print("---------------------------------")
# Print analysis to terminal
# #################################################################################

# Save analysis to file
output_file = os.path.join('.','data', 'output.txt')
with open(output_file, "w", newline="") as datafile:
    datafile.write("Election Results\n")
    datafile.write("---------------------------------\n")
    datafile.write(f"Total Votes:  {totalVotes} \n")
    for i in range(0,len(candidate)):
        datafile.write(f"{candidate[i]}:  {format(float(voteCount[i]/totalVotes)*100, '.3f')}% ({voteCount[i]})\n")
    datafile.write("---------------------------------\n")
    datafile.write(f"Winner:  {candidate[maxPopularVoteIndex]}\n")
    datafile.write("---------------------------------\n")
#################################################################################
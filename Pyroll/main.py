import os
import csv

csvpath = os.path.join('..', 'Pyroll', 'Resources', 'Voter.csv')

 # List store of data
votes_counted = 0
candidates = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    for row in csvreader:
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1
        votes_counted += 1

print("Election Results")
print("-------------------------")        
# The total number of votes cast
print("Total Votes:", votes_counted)
print("-------------------------")
# A complete list of candidates who received votes
print("Candidates who received votes:")
# The percentage of votes each candidate won
print("Vote percentages:")
for candidate, votes in candidates.items():
    percentage = (votes / votes_counted) * 100
    print(candidate + ":", f"{percentage:.3f}%", "(" + str(votes) +")")
print("--------------------------")  
# The winner of the election based on popular vote
winner = max(candidates, key=candidates.get)
print("Winner:", winner)
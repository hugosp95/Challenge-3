import os
import csv

filename = "PyPoll/Resources/election_data.csv"
output_file = "PyPoll/Analysis/election_analysis.txt"

#
with open(filename, 'r') as csvfile, open(output_file, 'w') as outputfile:
#with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    num_votes = 0 
    Diana_num_votes = 0
    Charles_num_votes = 0
    Raymon_num_votes = 0 
    winner = ("")

    candidates = {}

    for row in csvreader:
        num_votes += 1

        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

        if row[2] == "Charles Casper Stockham":
            Charles_num_votes += 1
        if row[2] == "Diana DeGette":
            Diana_num_votes += 1
        if row[2] == "Raymon Anthony Doane":
            Raymon_num_votes += 1
    if Diana_num_votes > Charles_num_votes and Diana_num_votes > Raymon_num_votes:
        winner = "Diana DeGette"
    elif Charles_num_votes > Diana_num_votes and Charles_num_votes > Raymon_num_votes:
        winner = "Charles Casper Stockham"
    else:
        winner = "Raymon Anthony Doane"


    print("Election Results")
    print("-" * 20)
    print("Total Votes: ",num_votes)
    print("-" * 20)
    for candidate, votes in candidates.items():
        percentage = round((votes*100/num_votes),3)
        print(f'{candidate} : {percentage}% ({votes})')
    print("-" * 20)
    print("Winner: ",winner)
    print("-" * 20)

    with open(output_file, 'w') as file:
        file.write("Election Results\n")
        file.write("-" * 20 + "\n")
        file.write(f"Total Votes: {num_votes}\n")
        file.write("-" * 20 + "\n")
        for candidate, votes in candidates.items():
            percentage = round((votes * 100 / num_votes), 3)
            file.write(f"{candidate}: {percentage}% ({votes})\n")
        file.write("-" * 20 + "\n")
        file.write(f"Winner: {winner}\n")
        file.write("-" * 20 + "\n")


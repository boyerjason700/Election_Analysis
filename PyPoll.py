# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candiates who recieved votes.
# 3. The percentage of votes each candiate won.
# 4. The total number of votes each candiate won.
# 5. The winner of the election based on popular vote.

import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save th file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initilize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)

    # Read and Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            #Append each candidate name to candidate list
            candidate_options.append(candidate_name)

#3. Print the total votes.
print(total_votes)

#Print candidate list
print(candidate_options)
















# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candiates who recieved votes.
# 3. The percentage of votes each candiate won.
# 4. The total number of votes each candiate won.
# 5. The winner of the election based on popular vote.

#Assign a variable for the file to load and the path
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)

import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Print the file object.
    print(election_data)

# #Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # #Write some data to the file.
    # txt_file.write("Hello World")

    # #Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")

    #Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")










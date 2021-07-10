# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee, Tom has given you the following tasks to complete the election audit of a recent local congressional election.  Along with some help from Tom's manager, Seth, we will find the following to produce the results of the audit.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

Additionally, the election commission has requested some additional data to complete the audit.

1. The voter turnout for each county.
2. The percentage of votes from each county out of the total count.
3. The county with the highest turnout.

## Resources
- Data Source: election_results.csv
- Software: 
    - [Python 3.6.1](https://www.python.org/)
    - [Visual Studio Code, 1.38.1](https://visualstudio.microsoft.com/vs/)

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
### County Results
- The county results were:
  - Jefferson county cast 10.5% of the vote and 38,855 number of votes.
  - Denver county cast 82.8% of the vote and 306,055 number of votes.
  - Arapahoe county cast 6.7% of the vote and 24,801 number of votes.
- The county with the largest number of votes was:
  - Denver county, who cast 82.8% of the vote and 306,055 number of votes.
### Candidate Results
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGatte received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGatte, who received 73.8% of the vote and 272,892 number of votes.
  
 ## Election-Audit Summary
 - This script can be used for future elections as is if the data imported is in the same format and data type.  Additional information can be obtained with modification to the code such as a specific county breakdown showing which candidate was more favored in each county.  
 - Likewise, it can be used with slight modification to accommodate additional data columns to provide a more detailed breakdown of the voting result.  For instance, collecting further demographics with each ballot (age, gender, party affiliation, etc.) would result in the ability to give a more detailed look into which candidate held more favor between the different demographics.
 

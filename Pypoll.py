# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
import os
import csv

file_to_load = os.path.join('C:/Users/Ashton/Desktop/Election Analysis/Resources/election_results.csv')
file_to_save = os.path.join('C:/Users/Ashton/Desktop/Election Analysis/Analysis/election_analysis.txt')

with open(file_to_load) as election_data:
     # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    print(headers)
# Git kinda sucks

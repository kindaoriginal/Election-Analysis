# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
import os
import csv

file_to_load = os.path.join('C:/Users/Ashton/Desktop/Classwork/Election Analysis Remote/Election-Analysis/Resources/election_results.csv')
file_to_save = os.path.join('C:/Users/Ashton/Desktop/Classwork/Election Analysis Remote/Election-Analysis/Analysis/election_analysis.txt')

counties = []

county_votes = {}

county_majority = ""

county_majority_count = 0

total_cvotes = 0

total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""

winning_count = 0

winning_percentage = 0

wc = ""

wcc = 0

wcp = 0


with open(file_to_load) as election_data:
     # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:
        
        total_votes += 1
        total_cvotes += 1
        candidate_name = row[2]
        county = row[1]
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1
    
    for county in counties:
        cvotes = county_votes[county]
        cvp = float(cvotes) / float(total_cvotes) * 100
        if county not in counties:
            counties.append(county)
            county_votes[county] = 0
        county_votes[county] += 1
        if (cvotes > wcc) and (cvp > wcp):



with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage

            winning_candidate = candidate_name
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary)
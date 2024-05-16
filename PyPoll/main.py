# Import relevant libraries
import os, csv

# Get absolute path of script
pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)

# Set the relative path to the input and output files
relative_path = os.path.join("PyPoll", "Resources","election_data.csv")
input_file = os.path.join("PyPoll", "Resources","election_data.csv")
output_file = os.path.join("PyPoll", "Analysis", "analysis.txt")

# Declare variables
total_votes = 0
candidate_votes = {}

# Read the file with UTF-8 encoding
with open(relative_path, 'r', encoding='UTF-8') as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        # Count total votes
        total_votes += 1
        
        # Get candidate name from row
        candidate_name = row["Candidate"]
        
        # Increse vote count for candidate
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Determine winner
winner = max(candidate_votes, key=candidate_votes.get)

# Write analysis to output file
with open(output_file, 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        f.write(f"{candidate}: {votes/total_votes*100:.3f}% ({votes})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")

# Print analysis to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes/total_votes*100:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
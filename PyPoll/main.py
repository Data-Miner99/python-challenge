# Import relevant libraries
import os, csv

# Get the absolute path of the script
pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)

# Set the relative path to the input and output files
relative_path = os.path.join("election_data.csv")
input_file = os.path.join("election_data.csv")
output_file = os.path.join("analysis.txt")

# Declare variables
total_votes = 0
candidate_list = []
candidate_votes_percent = []
total_candidate_votes = []
winner_by_votes = []

# Read the file with UTF-8 encoding
with open(relative_path, 'r', encoding='UTF-8') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            # Update total months and total revenue
            total_votes += 1

            candidate_name = row["Candidate"]
            
            # Calculate the revenue change
            if candidate_name not in candidate_list:
                candidate_list.append(candidate_name)
                candidate_votes_percent[candidate_name] = 0

                # Check for greatest increase and greatest decrease
                if change > greatest_increase[1]:
                    greatest_increase = [row["Date"], change]

                if change < greatest_decrease[1]:
                    greatest_decrease = [row["Date"], change]
            
            # Update previous revenue
            prev_rev = int(row["Profit/Losses"])
    
    # Calculate average change
avg_change = sum(rev_change) / len(rev_change) if rev_change else 0

    # Write results to output file
with open(output_file, 'w', encoding='UTF-8') as out_f:
        out_f.write("Financial Analysis\n")
        out_f.write("----------------------------\n")
        out_f.write(f"Total Months: {total_months}\n")
        out_f.write(f"Total Revenue: ${total_rev}\n")
        out_f.write(f"Average Revenue Change: ${avg_change:.2f}\n")
        out_f.write(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n")
        out_f.write(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the analysis in terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_rev}")
print(f"Average Revenue Change: ${avg_change:.2f}")
print(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})")
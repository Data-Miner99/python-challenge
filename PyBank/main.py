# Import relevant libraries
import os, csv

# Get the absolute path of the script
pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)

# Set the relative path to the input and output files
relative_path = os.path.join("PyBank", "Resources", "budget_data.csv")
input_file = os.path.join("PyBank", "Resources", "budget_data.csv")
output_file = os.path.join("PyBank", "Analysis", "analysis.txt")

# Declare variables
total_months = 0
prev_rev = 0
monthly_change = []
rev_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
total_rev = 0

# Read the file with UTF-8 encoding
with open(relative_path, 'r', encoding='UTF-8') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            # Update total months and total revenue
            total_months += 1
            total_rev += int(row["Profit/Losses"])
            
            # Calculate the revenue change
            if prev_rev is not 0:
                change = int(row["Profit/Losses"]) - prev_rev
                rev_change.append(change)
                monthly_change.append(row["Date"])

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
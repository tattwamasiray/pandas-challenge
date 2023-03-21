import os
import csv

# Path to the election data CSV file
election_csv_path = os.path.join("/Users/tattwamasiray/Downloads/Tat classin activity/BootCamp _Homework/python-challenge/PyPoll/Resources/election_data.csv")
# Initialize variables
total_votes = 0
candidates = {}
winner = ""

# Read the CSV file
with open(election_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # Skip header row

    # Loop through each row in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Determine the winner
max_votes = 0
for candidate, votes in candidates.items():
    percentage = votes / total_votes * 100
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = votes / total_votes * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a text file
output_path = os.path.join("election_results.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = votes / total_votes * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Results written to {output_path}")
import os
import csv

csv_path = os.path.join("/Users/tattwamasiray/Downloads/Tat classin activity/BootCamp _Homework/python-challenge/PyBank/Resources/budget_data.csv")

# Set the path for the csv file

import os
import csv

csv_path = os.path.join("/Users/tattwamasiray/Downloads/Tat classin activity/BootCamp _Homework/python-challenge/PyBank/Resources/budget_data.csv")

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change_list = []
greatest_profit_increase = ["", 0]
greatest_profit_decrease = ["", 9999999999999999999]

# Open the csv file and loop through the rows
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through the rows in the csv file
    for row in csvreader:

        # Calculate the total number of months included in the dataset
        total_months += 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        total_profit_loss += int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period, and add them to the list
        profit_loss_change = int(row[1]) - previous_profit_loss
        profit_loss_change_list.append(profit_loss_change)
        previous_profit_loss = int(row[1])

        # Calculate the greatest increase in profits (date and amount) over the entire period
        if profit_loss_change > greatest_profit_increase[1]:
            greatest_profit_increase[0] = row[0]
            greatest_profit_increase[1] = profit_loss_change

        # Calculate the greatest decrease in profits (date and amount) over the entire period
        if profit_loss_change < greatest_profit_decrease[1]:
            greatest_profit_decrease[0] = row[0]
            greatest_profit_decrease[1] = profit_loss_change

# Calculate the average of the changes in "Profit/Losses" over the entire period
average_profit_loss_change = sum(profit_loss_change_list) / len(profit_loss_change_list)

# Format the output for printing to the terminal and writing to the file
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_profit_loss_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_profit_increase[0]} (${greatest_profit_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_profit_decrease[0]} (${greatest_profit_decrease[1]})\n"
)

# Print the output to the terminal
print(output)

# Set the output file path
output_file = "budget_analysis.txt"

# Write the output to the output file
with open(output_file, "w") as textfile:
    textfile.write(output)




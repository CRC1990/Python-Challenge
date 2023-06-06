import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

total_months = []
total_profits = []
profit_changes = 0
monthly_changes = []
previous_value = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_reader= next(csvreader)
    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(row[1])

        print(len(total_months))
total_profits = [int(x) for x in total_profits]
total_profits_sum = sum(total_profits)
print(total_profits_sum)

for i in range(len(total_profits)-1):
    monthly_changes.append(total_profits[i+1]-total_profits[i])
    avg = sum(monthly_changes)/len(monthly_changes)


print("Average of the changes in Profit/Losses over the entire period:",avg)
maximum_profit  = max(monthly_changes)
minimum_profit  = min(monthly_changes)
index_of_maximum_profit  = monthly_changes.index(maximum_profit)
index_of_minimum_profit  = monthly_changes.index(minimum_profit)
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits}")

import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

output_file = os.path.join("analysis", "budget_analysis.txt")

total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change_list = []
greatest_increase = ['', 0]
greatest_decrease = ['', 99999999999]

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:("resources", "election_data.csv")

total_months += 1
total_profit_loss += int(row[1])

profit_loss_change = int(row[1]) - previous_profit_loss
profit_loss_change_list.append(profit_loss_change)
previous_profit_loss = int(row[1])

if profit_loss_change > greatest_increase[1]:
    greatest_increase[0] = row[0]
    greatest_increase[1] = profit_loss_change

if profit_loss_change < greatest_decrease[1]:
    greatest_decrease[0] = row[0]
    greatest_decrease[1] = profit_loss_change

average_profit_loss_change = sum(profit_loss_change_list[1:]) / len(profit_loss_change_list[1:])

print("Financial_Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_profit_loss_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

with open(output_file, "w") as txtfile:
    txtfile.write("Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_profit_loss_change:.2f}")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

 
print(analysis)

with open(output_file, "w") as file:
    file.write(analysis)

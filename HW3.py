import os
import csv

csvpath = os.path.join('/Users/user/Desktop/PythonStuff/SMU-VIRT-DATA-PT-12-2022-U-LOLC/02-Homework/03-Python/Starter_Code/PyBank/Resources/budget_data.csv')

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
print("Greatest increase in profits (date and amount) over the entire period:", total_months[index_of_maximum_profit + 1], maximum_profit )
print("Greatest decrease in losses (date and amount) over the entire period:", total_months[index_of_minimum_profit + 1], minimum_profit )




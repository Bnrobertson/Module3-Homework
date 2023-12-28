import os
import csv

csvpath = os.path.join('..','PyBank', 'Resources2', 'CData.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    # List store of data
    months = 0
    total_profit = 0
    previous_profit = 0
    list = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]

    for row in csvreader:
        months += 1
        profit = int(row[1])
        total_profit += profit

        if previous_profit != 0:
            change = profit - previous_profit
            list.append(change)

            # increase and decrease in profits
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        previous_profit = profit

    # average change
    average_change = sum(list) / len(list)

    # Print the financial analysis results
    print("Financial Analysis")
    print("----------------------------")
    # The total number of months included in the datasets
    print(f"Total Months: {months}")
    # The net total amount of "Profit/Losses" over the entire period
    print(f"Total: ${total_profit}")
   # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    print(f"Average Change: ${average_change:.2f}")
   # The greatest increase in profits (date and amount) over the entire period
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    # The greatest decrease in profits (date and amount) over the entire period
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


       
        







    
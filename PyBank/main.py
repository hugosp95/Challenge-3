import os
import os 
import csv

filename = "PyBank/Resources/budget_data.csv" 
output_file =  "PyBank/Analysis/budget_analysis.txt"

with open(filename, 'r') as csvfile, open(output_file, 'w') as outputfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    num_months = 0
    total_profit = 0
    previous_amount = 0
    sum_of_change = 0

    greatest_increase = 0
    greatest_decrease = 0

    month_greatest_increase = ""
    month_greatest_decrease = ""

    for row in csvreader:
        num_months += 1
        profit = int(row[1])
        total_profit += profit

        if previous_amount != 0:
            change = profit - previous_amount
            sum_of_change += change

            if change > greatest_increase:
                greatest_increase = change
                month_greatest_increase = row[0]
            
            if change < greatest_decrease:
                greatest_decrease = change
                month_greatest_decrease = row[0]
        
        previous_amount = profit

    av_change = sum_of_change / (num_months-1)

    print("Financial Analysis")
    print("-" * 20)
    print("Total Months:", num_months)
    print("Total: $", total_profit)
    print("Average Change: $", round(av_change, 2))
    print("Greatest Increase in Profits:", month_greatest_increase, "($", greatest_increase, ")")
    print("Greatest Decrease in Profits:", month_greatest_decrease, "($", greatest_decrease, ")")
    

    outputfile.write("Financial Analysis\n")
    outputfile.write("-" * 20 + "\n")
    outputfile.write("Total Months: " + str(num_months) + "\n")
    outputfile.write("Total: $" + str(total_profit) + "\n")
    outputfile.write("Average Change: $" + str(round(av_change, 2)) + "\n")
    outputfile.write("Greatest Increase in Profits: " + month_greatest_increase + " ($" + str(greatest_increase) + ")\n")
    outputfile.write("Greatest Decrease in Profits: " + month_greatest_decrease + " ($" + str(greatest_decrease) + ")\n")

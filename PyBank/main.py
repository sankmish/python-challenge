# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

import csv
import os

file = ("Resources/budget_data.csv")
outFile = ("Output/output_budget_data.txt")

date = []
plusMinus = []
netProfit = 0
totalChange = 0
greatestIncrease = 0
indexInc = 0
greatestDecrease = 0
indexDec = 0

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if (row == ""):
            break
        date.append(row[0])
        plusMinus.append(row[1])

# Calculate months from list of dates (-1 for blank last line)
months = len(date)-1
# Parse plusMinus into ints to add into Net
for z in range(1,months+1):
    plusMinus[z] = float(plusMinus[z])
# Calculate total Profit, average Profit greatest Increase and Decrease
for i in range(2,months+1):
    netProfit = netProfit + plusMinus[i]
    if (i == months):
        if (plusMinus[i] > plusMinus[i-1]):
            diffGreat = (plusMinus[i] - plusMinus[i-1])
            if (diffGreat > greatestIncrease):
                greatestIncrease = diffGreat
                indexInc = i
        if (plusMinus[i] < plusMinus[i-1]):
            diffLess = (plusMinus[i] - plusMinus[i-1])
            if (diffLess > greatestDecrease):
                greatestDecrease = diffLess
                indexDec = i
    if (i != months):
        if (plusMinus[i] > plusMinus[i-1]):
            diffGreat = (plusMinus[i] - plusMinus[i-1])
            if (diffGreat > greatestIncrease):
                greatestIncrease = diffGreat
                indexInc = 1
        if (plusMinus[i+1] < plusMinus[i]):
            diffLess = (plusMinus[i+1] - plusMinus[i])
            if (diffLess < greatestDecrease):
                greatestDecrease = diffLess
                indexDec = i
avgProf = netProfit/months

print("Financial Analysis:")
print("--------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(netProfit))
print("Average Change: $" + str(avgProf))
print("Greatest Increase in Profits: " + date[indexInc] + "  (" + str(greatestIncrease) +")" )
print("Greatest Decrease in Profits: " + date[indexDec] + "  (" + str(greatestDecrease) +")" )

with open(outFile, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis:"])
    writer.writerow(["--------------------------"])
    writer.writerow(["Total Months: " + str(months)])
    writer.writerow(["Total: $" + str(netProfit)])
    writer.writerow(["Average Change: $" + str(avgProf)])
    writer.writerow(["Greatest Increase in Profits: " + date[indexInc] + "  (" + str(greatestIncrease) +")" ])
    writer.writerow(["Greatest Decrease in Profits: " + date[indexDec] + "  (" + str(greatestDecrease) +")"])
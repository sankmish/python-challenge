import csv
import os

candidates = []
file = ("Resources/election_data.csv")
outFile = ("Output/output_election_data.txt")
uniqueNames = []
totalVotes = 0
countKhan = 0
countCorrey = 0 
countLi = 0
countTooley = 0

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if (row[2]=="Candidate"):
            continue
        candidates.append(row[2])
        if (row[2]=="Khan"):
            totalVotes = totalVotes + 1
            countKhan = countKhan + 1
        if (row[2]=="Correy"):
            totalVotes = totalVotes + 1
            countCorrey = countCorrey + 1
        if (row[2]=="Li"):
            totalVotes = totalVotes + 1
            countLi = countLi + 1
        if (row[2]=="O'Tooley"):
            totalVotes = totalVotes + 1
            countTooley = countTooley + 1
            
for x in candidates:
    if x not in uniqueNames:
        uniqueNames.append(x)
percentKhan = countKhan/totalVotes
percentCorrey = countCorrey/totalVotes
percentLi = countLi/totalVotes
percentTooley = countTooley/totalVotes
if (countKhan > countCorrey and countKhan > countLi and countKhan > countTooley):
    winner = "Khan"
if (countCorrey > countKhan and countCorrey > countLi and countCorrey and countTooley):
    winner = "Correy"
if (countLi > countKhan and countLi > countCorrey and countLi > countTooley):
    winner = "Li"
if (countTooley > countKhan and countTooley > countCorrey and countTooley > countLi):
    winner = "Tooley"
    
print("Election Results")
print("--------------------")
print("Total Votes: " + str(totalVotes) )
print("--------------------")
print(uniqueNames[0] + ": " +  "{:.3f}".format(percentKhan * 100)  + "% (" + str(countKhan) + ")")
print(uniqueNames[1] + ": " + "{:.3f}".format(percentCorrey * 100) + "% (" + str(countCorrey) + ")")
print(uniqueNames[2] + ": " + "{:.3f}".format(percentLi * 100) + "% (" + str(countLi) + ")")
print(uniqueNames[3] + ": " + "{:.3f}".format(percentTooley * 100) + "% (" + str(countTooley) + ")")
print("--------------------")
print("Winner: " + winner)
print("--------------------")


with open(outFile, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Election Results"]) 
    writer.writerow(["--------------------"])
    writer.writerow(["Total Votes: " + str(totalVotes)])
    writer.writerow(["--------------------"])
    writer.writerow([uniqueNames[0] + ": " +  "{:.3f}".format(percentKhan * 100)  + "% (" + str(countKhan) + ")"])
    writer.writerow([uniqueNames[1] + ": " + "{:.3f}".format(percentCorrey * 100) + "% (" + str(countCorrey) + ")"])
    writer.writerow([uniqueNames[2] + ": " + "{:.3f}".format(percentLi * 100) + "% (" + str(countLi) + ")"])
    writer.writerow([uniqueNames[3] + ": " + "{:.3f}".format(percentTooley * 100) + "% (" + str(countTooley) + ")"])
    writer.writerow(["--------------------"])
    writer.writerow(["Winner: " + winner])
    writer.writerow(["--------------------"])
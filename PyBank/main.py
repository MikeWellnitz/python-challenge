import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")
outputpath = os.path.join("analysis", "budget_analysis.txt")

# PyBank
# Number of Months in dataset (row count?)
months = []



# Net Total of P/L (sum of column B)
netPL = 0 #start this at 0 because just wanting to add up, not create a list


# Changes in P/L over period (?)
change_list = []

# 	-average of those changes (average function)
# Greatest increase in profits (date and amount) over the period
# Greatest decrease in profits (date and amount) over the period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)


with open(csvpath) as csvfile: #needs all this stuff and below

    csvreader = csv.reader(csvfile, delimiter=',')
     
    #print(csvreader)

    csv_header = next(csvreader) #when using next, it excludes the topmost record/row in the data . . . column header most likely. normally we want to exclude header row
    #print(f"CSV Header: {csv_header}")
    first_data_row = next(csvreader) #every time i used next, it is going to keep skipping a row. this is my 2nd next, so now things would start on row 3
    months.append(first_data_row[0])
    netPL = netPL + int(first_data_row[1])
    previous_value = int(first_data_row[1])

    for row in csvreader: #when you do a "for" loop, it casts "row" in this instance as a variable
       #print(row)
        months.append(row[0]) #this 0 here means look only at the first instance in the row. If it was 1, then it would show dollar amounts from data set
        netPL = netPL + int(row[1]) # in the data set right now in the Terminal below, the first number is in quotes meaning its a string. the int converts the value to an integer and the row[1] is meaning the second value in the row
        current_value = int(row[1])
        changePL = current_value - previous_value
        change_list.append(changePL)
        previous_value = int(row[1])

# months = len(list(csvreader))
#print(len(months))
#print(netPL)
averagechange = round(sum(change_list)/len(change_list),2)
#print(averagechange)
#print(max(change_list),min(change_list))
#print(change_list.index(max(change_list)),change_list.index(min(change_list)))
max_index = change_list.index(max(change_list))
min_index = change_list.index(min(change_list))
#print(months[max_index+1],months[min_index+1])

output = (f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(months)}\n"
f"Total: ${netPL}\n"
f"Average Change: ${averagechange}\n"
f"Greatest Increase in Profits: {months[max_index+1]} (${max(change_list)})\n"
f"Greatest Decrease in Profits: {months[min_index+1]} (${min(change_list)})")
print(output)

with open(outputpath,"w") as outputfile:
    outputfile.write(output)

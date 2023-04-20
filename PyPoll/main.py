import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")


# The total number of votes cast
votescast = []

# A complete list of candidates who received votes
candidates = []

# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote


with open(csvpath) as csvfile: #needs all this stuff and below

    csvreader = csv.reader(csvfile, delimiter=',')
     
    #print(csvreader)

    csv_header = next(csvreader) #when using next, it excludes the topmost record/row in the data . . . column header most likely. normally we want to exclude header row
    #print(f"CSV Header: {csv_header}")
    first_data_row = next(csvreader) #every time i used next, it is going to keep skipping a row. this is my 2nd next, so now things would start on row 3
    votescast.append(first_data_row[0])
    

    for row in csvreader: #when you do a "for" loop, it casts "row" in this instance as a variable
       #print(row)
        votescast.append(row[0])




output = (f"Election Results\n"
f" -------------------------\n"
f" Total Votes: {len(votescast)}\n")
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
#f" -------------------------)"
print(output)
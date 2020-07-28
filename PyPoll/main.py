import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    print(csv_header)
    
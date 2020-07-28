import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Analysis', 'financial_analysis.txt')
months = 0
total = 0
a_change = 0
maximum_change = 0
minimum_change = 0
maximum_index = 0
minimum_index = 0
max_month = ''
min_month = ''

mon_array =[]
num_array =[]

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    #For loop looking for items in csv(document) provided
    for individual_item in csvreader:
        #If variable in column 1 (0'th column) is not equal to the header...
        if (individual_item[0]) != "csv_header":
            #add one to the month count until you reach an empty row
            months += 1
            #add the contents in the 2nd column (1st column) to the total for every integer 
            total += int(individual_item[1])
            #create an array to track the individual value of the "profit/loss" column 
            num_array.append(individual_item[1])
            mon_array.append(individual_item[0])
    #create a variable to find the average difference in profit/loss per month
    a_change = total / months
    #create two variables to find the minimum and maximum values within the array
    maximum_change = max(num_array)
    minimum_change = min(num_array)
    #create indexes to track the min/max values of your indexed arrays
    maximum_index = num_array.index(maximum_change)
    minimum_index = num_array.index(minimum_change)
    #create variables to assign the min/max months for the min/max indexed arrays 
    max_month = mon_array[maximum_index]
    min_month = mon_array[minimum_index]
    
    output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${a_change}\n"
    f"Greatest Increase in Profits: {max_month} ${maximum_change}\n"
    f"Greatest Decrease in Profits: {min_month} ${minimum_change}\n")

    print(output)
    with open(output_path, 'w') as txtfile:
        txtfile.write(output)







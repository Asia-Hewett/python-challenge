import os 
import csv

employee_data = os.path.join('Resources', 'employee_data.csv')
output_path = os.path.join('PyBossExtraContent.txt')
employees = []
extra_content = ""

from Resources.state_abbreviation.us_state_abbrev import us_state_abbrev

from datetime import datetime

with open(employee_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        first = row[1].split()[0]
        last = row[1].split()[1]
        arbitrary = row[2]
        date = datetime.strptime(arbitrary, '%Y-%m-%d').strftime('%m/%d/%Y')
        new_ssn = "***-**-" + row[3].split("-")[2]
        new_state = us_state_abbrev.get(row[4]) 
        employees.append(
        {
            "Employee_ID": row[0], 
            "first_name": first,
            "last_name": last,
            "DOB": date,
            "SSN": new_ssn,
            "State": new_state
        })
    for redbull in employees:
        extra_content += f"{redbull.get('Employee_ID')},{redbull.get('first_name')},{redbull.get('last_name')},{redbull.get('DOB')},{redbull.get('SSN')},{redbull.get('State')}\n"
        
        
        output = (
    f"Emp ID,First Name,Last Name,DOB,SSN,State\n"
    f"{extra_content}\n"
        )

    print(output)
    with open(output_path, 'w') as txtfile:
        txtfile.write(output)




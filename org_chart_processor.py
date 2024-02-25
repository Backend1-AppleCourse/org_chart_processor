import json

# Specify the path to your JSON file
file_path = 'companies.json'

# Open the JSON file for reading
with open(file_path, 'r') as file:
    # Parse the JSON file content into a Python dictionary
    companies = json.load(file)

def get_employees_total(employee, worker_num=0):
    worker_num = worker_num + 1
    name = employee['name']


    if 'subordinates' in employee:
        for emp in employee['subordinates']:
            worker_num = get_employees_total(emp, worker_num=worker_num)

    return worker_num

        

# print(get_employees_total(companies[0]))

def get_CTO_subordinates(employee, subordinates=[], under_CTO=False):
    name = employee['name']

    if(name == 'CTO'):
        under_CTO = True

    if under_CTO:
        if 'subordinates' in employee:
            for sub in employee['subordinates']:
                subordinates.append(sub['name'])
                subordinates = get_CTO_subordinates(sub, subordinates=subordinates, under_CTO=True)
    else:
        if 'subordinates' in employee:
            for sub in employee['subordinates']:
                subordinates = get_CTO_subordinates(sub)
            
    return subordinates

# print(get_CTO_subordinates(companies[0]))

def dev_total_in_title(employee, title, dev_num=0):
    name = employee['name']

    if title in employee['name']:
        dev_num = dev_num + 1

    if 'subordinates' in employee:
        for emp in employee['subordinates']:
            dev_num = dev_total_in_title(emp, title, dev_num=dev_num)

    return dev_num

# print(dev_total_in_title(companies[2], 'Developer'))

def get_departments(employee, departments=[]):
    name = employee['name']
    department = True

    if 'subordinates' in employee:
        for sub in employee['subordinates']:
            if 'subordinates' in sub:
                department = False
                departments = get_departments(sub, departments=departments)
        if(department):
            departments.append(name)
    return departments

# print(get_departments(companies[0]))

def process_org_chart(companies, title='Developer'):
    for i, company in enumerate(companies):
        print(f"Company: {i}")
        print(f"Total employees: {get_employees_total(company)}")
        print(f"CTO subordinates: {get_CTO_subordinates(company)}")
        print(f"Total developers: {dev_total_in_title(company, title)}")
        print(f"Departments: {get_departments(company)}")
        print("\n")

process_org_chart(companies)




            
# Define a dictionary with Emp IDs as keys and salaries as values
employees = {
    1001: 25000,
    1002: 27000,
    1003: 22000,
    1004: 30000,
    1005: 28000,
    1006: 35000,
    1007: 26000,
    1008: 29000,
    1009: 31000,
    1010: 27000
}

for emp_id, salary in employees.items():
    if salary>30000:
        print(f"Employee ID {emp_id}: Salary {salary}")

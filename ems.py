from employee import Employee
from datetime import datetime

employees = [] 

def read_employees():
    option = input("""Select option:
    1: See all employees
    2: Find Employee by id
    3: Find Employees by department""")
    match option:
        case "1":  
            for employee in employees: print(employee)
        case "2": 
            emp_id = input("Enter employee id: ")
            for employee in employees: 
                if str(employee.emp_id) == emp_id: 
                    print(employee)
                    break
                else: print(f"No employee with id {id} found.")
        case "3":
            department = input("Enter Department")
            dept = [str(employee) for employee in employees if employee.department == department]
            for employee in dept: 
                print(employee)
        case _ : print("Not a valid input.")


if __name__ == "__main__":
    while True:
        print("""Welcome to the Employee Management System!  Please enter an option:
        1: See Employees
        2: Add Employees
        3: Update an Employee
        4: Remove an Employee
        5: exit""")  
        option = input("option: ")

        match option:
            case "1": read_employees()
            case "2": break
            case _ : print("Not a valid input.")
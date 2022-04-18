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


def add_employee():
    first_name = input("Enter employee first name ")
    last_name = input("Enter emplyee last name: ")
    
    while True:
        try: 
            salary = int(input("Enter emplyee salary: "))
        except ValueError:
            print("Salary must be an integer")
        else: break
    
    while True:
        try: 
            doe_string = input("Enter emplyee date of employment (day/month/year): ")
            doe = datetime.strptime(doe_string, "%d/%m/%Y")
        except ValueError:
            print("Date must be in the format day/month/full year")
        else: break
    department = input("Enter emplyee department: ")

    employee = Employee(first_name, last_name, salary, doe, department)
    employees.append(employee)


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
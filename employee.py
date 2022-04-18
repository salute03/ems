class Employee:
    emp_count = 0

    def __init__(self, first_name, last_name, salary, doe, department):
        Employee.emp_count += 1
        self.first_name = first_name
        self.last_name  = last_name
        self.salary = salary
        self.doe = doe
        self.department = department
        self.emp_id = Employee.emp_count
    
    def __str__(self):
        return f"""-----
        Employee ID: {self.emp_id}
        Name: {self.first_name} {self.last_name}
        Salary: {self.salary}
        Date of Employment: {self.doe.date()}
        Department: {self.department}
        -----"""








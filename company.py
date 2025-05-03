from employee import Employee

class Company:
    def __init__(self):
        self.employee = []

    def add_employee(self, new_employee):
            self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employee:")
        for i in self.employees:
             print(i.fname, i.lname)
        print("--------------------")

    def pay_employee(self):
         print("Paying Employees:")
         for i in self.employees:
              print("Paycheck for:", i.fname, i.lname)
              print("amount:", i.calculate_paycheck())
              print("---------------------------")



def main():
    my_company = Company()

    employee1 = Employee("Sarah", "Rochon", 50000)
    my_company.add_employee(employee1)
    employee2 = Employee("Keisha", "Rochon", 60000)
    my_company.add_employee(employee2)
    employee3 = Employee("Aaron ", "Rochon", 70000)
    my_company.add_employee(employee3)

    my_company.display_employees()

main()
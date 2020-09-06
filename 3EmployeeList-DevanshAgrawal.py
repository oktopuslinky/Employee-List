import csv, tkinter, shutil
from tempfile import NamedTemporaryFile

class EmployeeList:
    def __init__(self):
        self.user_input=""
        self.display_main_menu()

    def display_main_menu(self):
        print(
            """
                Hello!
                1) Add an employee to the system
                2) Delete an employee from the system
                3) Sort employees
                4) Search for an employee
                5) Save the file
                6) Display all employees
                7) Quit
            """
        )
        self.user_input=int(input("Enter number for choice: "))

    def redirect_user(self):
        if type(self.user_input) == int:
            if self.user_input == 1:
                ###add choices
                pass
        else:
            print("Please enter a number.")
            self.display_main_menu()

the_employee_list=EmployeeList()
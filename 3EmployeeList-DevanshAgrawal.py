import csv, tkinter, shutil
from tempfile import NamedTemporaryFile

class EmployeeList:
    def __init__(self):
        self.user_input = ""
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
        self.user_input=self.take_input("int")

    def take_input(self, data_type):
        if data_type == "int":
            while True:
                try:
                    self.user_input = int(input('Insert choice: '))
                    break
                except:
                    print("try again")
        
        elif data_type == "string":
            while True:
                try:
                    self.user_input = str(input("Insert choice: "))
                    break
                except:
                    print("try again")

    def redirect_user(self):
        if type(self.user_input) == int:
            if self.user_input == 1:
                #add
                pass
            elif self.user_input == 2:
                #delete
                pass
            elif self.user_input == 3:
                #sort
                pass
            elif self.user_input == 4:
                #search
                pass
            elif self.user_input == 5:
                #save
                pass
            elif self.user_input == 6:
                #display
                pass
            elif self.user_input == 7:
                #quit
                pass
        else:
            print("Please enter a number from 1-7.")
            self.display_main_menu()

the_employee_list = EmployeeList()
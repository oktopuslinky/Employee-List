import csv, tkinter, shutil
import tempfile
from tempfile import NamedTemporaryFile

class EmployeeList:
    def __init__(self):
        self.user_input = ""
        self.employee_list = []
        self.file_to_list()
        self.display_main_menu()

    def display_main_menu(self):
        print(
            """
                Welcome to the employee list!

                1) Add an employee to the system
                2) Delete an employee from the system
                3) Sort employees
                4) Search for an employee
                5) Save the file
                6) Display all employees
                7) Quit
            """
        )
        self.take_input("int")
        self.redirect_user_main()

    def display_sort_menu(self):
        print(
            """
                Sort employees:

                1) Alphabetically by first name
                2) Alphabetically by last name
                3) By level
                4) By job position
                5) Chronologically by date hired
                6) Ascending by pay
                7) Cancel sort
            """
        )
        self.take_input("int")
        self.redirect_user_sort()

    def file_to_list(self):
        with open("employees.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            self.employee_list = list(reader)

    def take_input(self, data_type):
        if data_type == "int":
            while True:
                try:
                    self.user_input = int(input('Insert choice: '))
                    break
                except:
                    print("Try again")
        
        elif data_type == "string":
            while True:
                try:
                    self.user_input = str(input("Insert choice: "))
                    break
                except:
                    print("Try again")

    def redirect_user_sort(self):
        if type(self.user_input) == int:
            if self.user_input != 7:
                if self.user_input == 1:
                    #first
                    pass
                elif self.user_input == 2:
                    #last
                    pass
                elif self.user_input == 3:
                    #level
                    pass
                elif self.user_input == 4:
                    #job position
                    pass
                elif self.user_input == 5:
                    #date hired
                    pass
                elif self.user_input == 6:
                    #pay
                    pass
            else:
                self.display_main_menu()

    def redirect_user_main(self):
        if type(self.user_input) == int:
            if self.user_input != 7:
                if self.user_input == 1:
                    self.add_emp()
                    pass
                elif self.user_input == 2:
                    self.delete_emp()
                    pass
                elif self.user_input == 3:
                    self.sort_emp()
                    pass
                elif self.user_input == 4:
                    self.search_emp()
                    pass
                elif self.user_input == 5:
                    self.save_file()
                    pass
                elif self.user_input == 6:
                    self.display_emp()
                    pass
            else:
                print("Have a nice day.")
                return
        else:
            print("Please enter a number from 1-7.")
            self.display_main_menu()


    def add_emp(self):
        pass

    def delete_emp(self):
        pass

    def sort_emp(self):
        pass
    
    def search_emp(self):
        pass

    def save_file(self):
        filename = "employees.csv"
        with open(filename, "w") as csvfile:
            headers = ["Name", 'Level', 'Date Hired', 'Pay', "Job Position", "Date Departed"]
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in self.employee_list:
                writer.writerow(row)
        csvfile.close()
        print("The file has been saved.")
        input("Press ENTER")
        self.display_main_menu()

    def display_emp(self):
        print(self.employee_list)

the_employee_list = EmployeeList()
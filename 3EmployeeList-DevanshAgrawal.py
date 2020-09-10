import csv
from operator import itemgetter

class EmployeeList():
    def __init__(self):
        self.employee_list = []

        print(self.employee_list)
        print("----")
        if len(self.employee_list) == 0:
            print("zero")
            self.file_to_list()

        print(self.employee_list)

    def file_to_list(self):
        with open("employees.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.employee_list.append(row)

    def sort_emp(self, sort_key):
        temp_emp_list = self.employee_list
        if len(temp_emp_list) > 0:
            temp_emp_list.sort(key=itemgetter(sort_key))
            print(temp_emp_list)

        input("Press ENTER")
        self.display_main_menu()

    def search_emp(self, search_name):
        for emp in self.employee_list:
            if emp['Name'] == search_name:
                return emp

class Employee(EmployeeList):
    def __init__(self):
        super().__init__()
        self.new_name = ''
        self.new_level = ''
        self.new_month = 0
        self.new_day = 0
        self.new_year = 0
        self.new_date = ''
        self.new_pay = 0
        self.new_position = ''
        
        #Name, Level, Date, Pay, Position, Departed
        self.max_lengths = [0, 0, 0, 0, 0, 0]
        
    def add_emp(self):
        print("Please input the following information about the new employee:")

        while True:
            while True:
                try:
                    self.new_name = str(input("Name: "))
                    break
                except:
                    print("try again.")

            emp_data = super().search_emp(self.new_name)
            if emp_data is not None and not emp_data['Date Departed']:
                print("This employee already exists. Please try again.")
            else:
                break
        
        while True:
            try:
                self.new_level = str(input("Level: "))
                break
            except:
                print("Try again.")

        while True:
            while True:
                try:
                    self.new_month = int(input("Month (MM): "))
                    break
                except:
                    print("Try again.")

            if len(str(self.new_month)) == 2:
                break
            else:
                print("Please input two integers.")

        while True:
            while True:
                try:
                    self.new_day = int(input("Day (DD): "))
                    break
                except:
                    print("Try again.")

            if len(str(self.new_day)) == 2:
                break
            else:
                print("Please input two integers.")

        while True:
            while True:
                try:
                    self.new_year = int(input("Year (YYYY): "))
                    break
                except:
                    print("Try again.")

            if len(str(self.new_year)) == 4:
                break
            else:
                print("Please input four integers.")
        
        while True:
            try:
                self.new_pay = int(input("Pay: $"))
                break
            except:
                print("Try again.")
            
        self.new_pay = str(self.new_pay)

        while True:
            try:
                self.new_position = str(input("Position: "))
                break
            except:
                print("Try again.")

        self.new_date = str(str(self.new_year)+"-"+str(self.new_month)+"-"+str(self.new_day))

        (self.employee_list).append({
            "Name": self.new_name,
            "Level": self.new_level,
            "Date Hired": self.new_date,
            "Pay": self.new_pay,
            "Job Position": self.new_position,
            "Date Departed": None
        })

        print("This employee has been added to the system.")
        input("Press ENTER")
        Menu().display_main_menu()

    def delete_emp(self):
        while True:
            Menu.take_input("string", "What is the name of this employee")
            emp_data = super().search_emp(self.user_input)
            employee_index = None
            for index in range(len(self.employee_list)):
                #print(self.employee_list[index])
                if self.employee_list[index] == emp_data:
                    print("Found a Match!")
                    employee_index = index

            if employee_index:
                break

        departed_year = input("What year did the employee depart?: ")
        departed_month = input("what month did the employee depart?:")
        departed_day = input("what day of the month did the employee depart?")
        final_date = str(str(departed_year)+"-"+str(departed_month)+"-"+str(departed_day))

        self.employee_list[employee_index]['Date Departed'] = final_date

        print("Employee ")
        input("Press ENTER")
        self.display_main_menu()
        
    def display_emp(self):
        self.get_max_lengths()
        print(
            "╔" + (self.max_lengths[0] * "═") +
            "╦" + (self.max_lengths[1] * "═") +
            "╦" + (self.max_lengths[2] * "═") +
            "╦" + (self.max_lengths[3] * "═") +
            "╦" + (self.max_lengths[4] * "═") +
            "╦" + (13 * "═") +
            "╗"
            )
        print(
            "║" + 
            "Name" + " " * (self.max_lengths[0]-4) + "║" + 
            "Level" + " " * (self.max_lengths[1]-5) + "║" + 
            "Date Hired" + "║" + 
            "Pay" + " " * (self.max_lengths[3]-3) + "║" + 
            "Job position" + " " * (self.max_lengths[4]-12) + "║" + 
            "Date Departed" + "║"
        )
        input("Press ENTER")
        Menu().display_main_menu()

    def get_max_lengths(self):
        for row in self.employee_list:
            if len(row['Name']) > self.max_lengths[0]:
                self.max_lengths[0] = len(row['Name'])
            
            if len(row['Level']) > self.max_lengths[1]:
                self.max_lengths[1] = len(row['Level'])

            if len(row['Date Hired']) > self.max_lengths[2]:
                self.max_lengths[2] = len(row['Date Hired'])

            if len(row['Pay']) > self.max_lengths[3]:
                self.max_lengths[3] = len(row['Pay'])

            if len(row['Job Position']) > self.max_lengths[4]:
                self.max_lengths[4] = len(row['Job Position'])
            
            if len(row['Date Departed']) > self.max_lengths[5]:
                self.max_lengths[5] = len(row['Date Departed'])

class File(EmployeeList):
    def __init__(self):
        super().__init__()
        self.file = "employees.csv"

    def save_file(self):
        with open(self.file, "w") as csvfile:
            headers = ["Name", 'Level', 'Date Hired', 'Pay', "Job Position", "Date Departed"]
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in self.employee_list:
                writer.writerow(row)
        csvfile.close()

        print("The file has been saved.")
        input("Press ENTER")
        Menu().display_main_menu()

class Menu(EmployeeList):
    def __init__(self):
        #super().__init__()
        self.user_input = ""
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
        self.take_input("int", "Insert choice")
        self.redirect_user_main()

    def display_sort_menu(self):
        print(
            """
                Sort employees:

                1) Alphabetically by name
                2) By level
                3) By job position
                4) Chronologically by date hired
                5) Ascending by pay
                6) Chronologically by date departed
                7} Cancel sort
            """
        )

    def take_input(self, data_type, input_text):
        if data_type == "int":
            while True:
                try:
                    self.user_input = int(input(input_text+": "))
                    break
                except:
                    print("Try again")
        
        elif data_type == "string":
            while True:
                try:
                    self.user_input = str(input(input_text+": "))
                    break
                except:
                    print("Try again")

    def redirect_user_sort(self):
        if type(self.user_input) == int:
            if self.user_input != 7:
                if self.user_input == 1:
                    self.sort_emp("Name")

                elif self.user_input == 2:
                    self.sort_emp("Level")
                    
                elif self.user_input == 3:
                    self.sort_emp("Job Position")
                    
                elif self.user_input == 4:
                    self.sort_emp("Date Hired")
                    
                elif self.user_input == 5:
                    self.sort_emp("Pay")

                elif self.user_input == 6:
                    self.sort_emp("Date Departed")
            else:
                self.display_main_menu()

    def redirect_user_main(self):
        if type(self.user_input) == int:
            if self.user_input != 7:

                if self.user_input == 1:
                    Employee().add_emp()

                elif self.user_input == 2:
                    Employee().delete_emp()

                elif self.user_input == 3:
                    self.display_sort_menu()
                    self.take_input("int", "Insert choice")
                    self.redirect_user_sort()
                    
                elif self.user_input == 4:
                    searching_name = str(input("What is the name of this employee?: "))
                    employee_data = super().search_emp(searching_name)
                    if employee_data is not None:
                        print(employee_data)
                    else:
                        print("This employee does not exist.")
                    
                    input("Press ENTER")
                    self.display_main_menu()

                elif self.user_input == 5:
                    File().save_file()
                    
                elif self.user_input == 6:
                    Employee().display_emp()
                    
            else:
                print("Have a nice day.")
                return
        else:
            print("Please enter a number from 1-7.")
            self.display_main_menu()

the_employee_list = EmployeeList()
the_menu = Menu()
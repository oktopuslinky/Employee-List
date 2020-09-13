import csv, sys
from operator import itemgetter

class EmployeeList(object):
    def __init__(self, employee_list=None):
        if employee_list is None:
            self.employee_list = []
            self.file_to_list()
        elif employee_list is not None:
            self.employee_list = employee_list

    def file_to_list(self):
        with open("employees.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.employee_list.append(row)

    def sort_emp(self, sort_key, the_employee_list):
        temp_emp_list = EmployeeList(the_employee_list).employee_list
        if len(temp_emp_list) > 0:
            temp_emp_list.sort(key=itemgetter(sort_key))

        Employee(self.the_employee_list).display_emp(temp_emp_list)
        input("Press ENTER")
        self.display_main_menu()

    def search_emp(self, search_name):
        for emp in self.employee_list:
            if emp['Name'] == search_name:
                return emp

class Employee(EmployeeList):
    def __init__(self, the_employee_list):
        self.the_employee_list = the_employee_list

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
            self.new_name = Menu(self.the_employee_list).take_input("string", "Name")

            emp_data = EmployeeList(self.the_employee_list).search_emp(self.new_name)
            if emp_data is not None and not emp_data['Date Departed']:
                print("This employee already exists. Please try again.")
            else:
                break

        self.new_level = Menu(self.the_employee_list).take_input("string", "Level")

        self.new_month = Menu(self.the_employee_list).take_input("int", "Month (MM)")
        self.new_month = f'{self.new_month:02}'

        self.new_day = Menu(self.the_employee_list).take_input("int", "Day (DD)")
        self.new_day = f'{self.new_day:02}'

        while True:
            self.new_year = Menu(self.the_employee_list).take_input("int", "Year (YYYY)")
            if len(str(self.new_year)) == 4:
                break
            else:
                print("Please input four integers.")

        self.new_pay = Menu(self.the_employee_list).take_input("money", "Pay")
        self.new_pay = str(self.new_pay)

        self.new_position = Menu(self.the_employee_list).take_input("string", "Position")

        self.new_date = str(str(self.new_year)+"-"+str(self.new_month)+"-"+str(self.new_day))

        final_input = Menu(self.the_employee_list).take_input("verify", "Are you sure you want to add this new employee?")

        if final_input == "y" or final_input == "Y":
            (self.the_employee_list).append({
                "Name": self.new_name,
                "Level": self.new_level,
                "Date Hired": self.new_date,
                "Pay": self.new_pay,
                "Job Position": self.new_position,
                "Date Departed": ''
            })
            print("This employee has been added to the system.")
            input("Press ENTER")
        else:
            print("You will now be redirected to the main menu.")

        Menu(self.the_employee_list).display_main_menu()

    def delete_emp(self):
        while True:
            the_user_input = Menu(self.the_employee_list).take_input("string", "What is the name of this employee")
            emp_data = EmployeeList(self.the_employee_list).search_emp(the_user_input)
            employee_index = None
            for index in range(len(self.the_employee_list)):
                if self.the_employee_list[index] == emp_data:
                    print("Found a Match!")
                    employee_index = index

            if employee_index:
                break

        while True:
            departed_year = Menu(self.the_employee_list).take_input("int", "What year did the employee depart? (YYYY)")
            if len(str(departed_year)) == 4:
                break
            else:
                print("Please input four integers.")

        departed_month = Menu(self.the_employee_list).take_input("int", "what month did the employee depart?")
        departed_month = f'{departed_month:02}'

        departed_day = Menu(self.the_employee_list).take_input("int", "what day of the month did the employee depart?")
        departed_day = f'{departed_day:02}'

        final_date = str(str(departed_year)+"-"+str(departed_month)+"-"+str(departed_day))

        final_choice = Menu(self.the_employee_list).take_input("verify", "Are you sure you want to delete this employee?")

        if final_choice == "Y" or final_choice == "y":
            self.the_employee_list[employee_index]['Date Departed'] = final_date
            print("Employee deleted.")
            input("Press ENTER")
        else:
            print("You will now be redirected to the main menu.")

        Menu(self.the_employee_list).display_main_menu()
        
    def display_emp(self, the_employee_list):
        self.get_max_lengths(the_employee_list)
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
            "Job Position" + " " * (self.max_lengths[4]-12) + "║" + 
            "Date Departed" + "║"
        )
        print(
            "╠" + (self.max_lengths[0] * "═") +
            "╬" + (self.max_lengths[1] * "═") +
            "╬" + (self.max_lengths[2] * "═") +
            "╬" + (self.max_lengths[3] * "═") +
            "╬" + (self.max_lengths[4] * "═") +
            "╬" + (13 * "═") +
            "╣"
        )
        for emp in the_employee_list:
            print(
                "║" + emp['Name'] + ' ' * (self.max_lengths[0] - len(emp['Name'])) +
                "║" + emp["Level"] + ' ' * (self.max_lengths[1] - len(emp['Level'])) +
                "║" + emp['Date Hired'] + ' ' * (self.max_lengths[2] - len(emp['Date Hired'])) +
                "║" + emp['Pay'] + ' ' * (self.max_lengths[3] - len(emp['Pay'])) +
                "║" + emp['Job Position'] + ' ' * (self.max_lengths[4] - len(emp['Job Position'])) +
                "║" + emp['Date Departed'] + ' ' * (13 - len(emp['Date Departed'])) +
                "║"
            )
        print(
            "╚" + (self.max_lengths[0] * "═") +
            "╩" + (self.max_lengths[1] * "═") +
            "╩" + (self.max_lengths[2] * "═") +
            "╩" + (self.max_lengths[3] * "═") +
            "╩" + (self.max_lengths[4] * "═") +
            "╩" + (13 * "═") +
            "╝"
        )
        print(" ")
        input("Press ENTER")
        Menu(self.the_employee_list).display_main_menu()

    def get_max_lengths(self, the_employee_list):
        for row in the_employee_list:
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
        
        #self.max_lengths 2 and 5 are irrelevant since they aren't affected by small values.
        if self.max_lengths[0] < 4:
            self.max_lengths[0] = 4

        if self.max_lengths[1] < 5:
            self.max_lengths[1] = 5
        
        if self.max_lengths[3] < 3:
            self.max_lengths[3] = 3
        
        if self.max_lengths[4] < 12:
            self.max_lengths[4] = 12

class File(EmployeeList):
    def __init__(self, the_employee_list):
        self.file = "employees.csv"
        self.the_employee_list = the_employee_list

    def save_file(self):
        final_input = Menu(self.the_employee_list).take_input("verify", "Are you sure you want to save the file?")
        if final_input == "Y" or final_input == "y":
            with open(self.file, "w") as csvfile:
                headers = ["Name", 'Level', 'Date Hired', 'Pay', "Job Position", "Date Departed"]
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                for row in self.the_employee_list:
                    writer.writerow(row)
            csvfile.close()

            print("The file has been saved.")
            input("Press ENTER")
        else:
            print("You will now be redirected to the main menu.")

        Menu(self.the_employee_list).display_main_menu()

class Menu(EmployeeList):
    def __init__(self, the_employee_list):
        self.the_employee_list = the_employee_list

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
        the_user_input = self.take_input("int", "Insert choice")
        final_user_input = self.take_input("verify", "Are you sure about this choice?")
        if final_user_input == "Y" or final_user_input == "y":
            self.redirect_user_main(the_user_input)
        else:
            self.display_main_menu()

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
        the_user_input = self.take_input("int", "Insert choice")
        final_user_input = self.take_input("verify", "Are you sure about this choice?")
        if final_user_input == "Y" or final_user_input == "y":
            self.redirect_user_sort(the_user_input)
        else:
            self.display_sort_menu()

    def take_input(self, data_type, input_text):
        if data_type == "int":
            while True:
                try:
                    user_input = int(input(input_text + ": "))
                    if user_input is not None:
                        break
                except:
                    print("Please try again.")
            return user_input
        
        elif data_type == "string":
            while True:
                try:
                    user_input = str(input(input_text + ": "))
                    if user_input is not None:
                        break
                except:
                    print("Please try again.")
            return user_input

        elif data_type == "money":
            while True:
                try:
                    user_input = int(input(input_text + ": $"))
                    if user_input is not None:
                        break
                except:
                    print("Please try again.")

            user_input = f'{user_input:,}'
            user_input = "$" + str(user_input)
            return user_input

        elif data_type == "verify":
            possible_values = ["Y", "N", "y", "n"]
            while True:
                try:
                    user_input = str(input(input_text + " (Y/N): "))
                    if user_input is not None and user_input in possible_values:
                        break
                except:
                    print("Please try again.")
            return user_input

    def redirect_user_sort(self, user_input):
        possible_choices = [1, 2, 3, 4, 5, 6, 7]
        if type(user_input) == int and user_input in possible_choices:
            if user_input == 1:
                self.sort_emp("Name", self.the_employee_list)

            elif user_input == 2:
                self.sort_emp("Level", self.the_employee_list)
                
            elif user_input == 3:
                self.sort_emp("Job Position", self.the_employee_list)
                
            elif user_input == 4:
                self.sort_emp("Date Hired", self.the_employee_list)
                
            elif user_input == 5:
                self.sort_emp("Pay", self.the_employee_list)

            elif user_input == 6:
                self.sort_emp("Date Departed", self.the_employee_list)

            elif user_input == 7:
                self.display_main_menu()
        else:
            print("Please input an integer from 1-7.")
            self.display_sort_menu()

    def redirect_user_main(self, user_input):
        possible_choices = [1, 2, 3, 4, 5, 6, 7]
        if type(user_input) == int and user_input in possible_choices:
            if user_input == 1:
                Employee(self.the_employee_list).add_emp()

            elif user_input == 2:
                Employee(self.the_employee_list).delete_emp()

            elif user_input == 3:
                self.display_sort_menu()
                the_user_input = self.take_input("int", "Insert choice")
                self.redirect_user_sort(the_user_input)
                
            elif user_input == 4:
                searching_name = self.take_input("string", "What is the name of this employee?")
                employee_data = EmployeeList(self.the_employee_list).search_emp(searching_name)
                if employee_data is not None:
                    the_employee_data = [employee_data]
                    Employee(self.the_employee_list).display_emp(the_employee_data)
                else:
                    print("This employee does not exist.")
                
                input("Press ENTER:")
                self.display_main_menu()

            elif user_input == 5:
                File(self.the_employee_list).save_file()
                
            elif user_input == 6:
                Employee(self.the_employee_list).display_emp(self.the_employee_list)
            
            elif user_input == 7:
                print("Have a nice day.")
                sys.exit()
        else:
            print("Please enter an integer from 1-7.")
            self.display_main_menu()

the_employees = EmployeeList()
the_menu = Menu(the_employees.employee_list)
the_menu.display_main_menu()
import csv, sys
from operator import itemgetter

class EmployeeList(object):
    def __init__(self):
        self.employee_list_cur = []
        self.employee_list_dep = []

        self.create_lists()

    def create_lists(self):
        with open("employees.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Date Departed'] == "":
                    self.employee_list_cur.append(row)
                else:
                    self.employee_list_dep.append(row)

        return(self.employee_list_cur, self.employee_list_dep)

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

class File():
    #MAKE READER

    def __init__(self, the_employee_list):
        self.file = "employees.csv"
        self.the_employee_list = the_employee_list
        self.file_reader()

    def file_reader(self):
        with open(self.file, "r") as csvfile:
            self.the_employee_list = list(csv.DictReader(csvfile))
            print(self.the_employee_list)

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

class Menu():
    #read, disp file from menu
    def __init__(self):
        self.employee_list = list()
        self.file_object = File(None)
        self.done = False

        self.user_choice = 0

    def run(self):
        #YOU CAN CREATE OBJECTS IN CLASSES

        #read file
        #add to list
        #while not self.done:
            #disp menu
            #get input
            #take action from input

        print("running.")
        #file is read into a list.
        self.employee_list = self.file_object.file_reader()

        while self.done == False:
            self.display_main_menu()

            possible_choices = [1, 2, 3, 4, 5, 6, 7]
            input_valid = False

            while input_valid is False:
                self.user_choice = Take_input("int", "Insert Choice").the_user_input
                if self.user_choice in possible_choices and type(self.user_choice) == int:
                    input_valid = True
                else:
                    print("Please input an integer from 1-7.")

            self.redirect_user()

    def redirect_user(self):
        if self.user_choice != 3:
            if self.user_choice == 1:
                Employee(self.the_employee_list).add_emp()

            elif self.user_choice == 2:
                Employee(self.the_employee_list).delete_emp()

            elif self.user_choice == 3:
                self.display_sort_menu()
                the_user_input = self.take_input("int", "Insert choice")
                self.redirect_user_sort(the_user_input)
                
            elif self.user_choice == 4:
                searching_name = self.take_input("string", "What is the name of this employee?")
                employee_data = EmployeeList(self.the_employee_list).search_emp(searching_name)
                if employee_data is not None:
                    the_employee_data = [employee_data]
                    Employee(self.the_employee_list).display_emp(the_employee_data)
                else:
                    print("This employee does not exist.")
                
                input("Press ENTER:")
                self.display_main_menu()

            elif self.user_choice == 5:
                File(self.the_employee_list).save_file()
                
            elif self.user_choice == 6:
                Employee(self.the_employee_list).display_emp(self.the_employee_list)
            
            elif self.user_choice == 7:
                print("Have a nice day.")
                sys.exit()

        elif self.user_choice == 3:
            if self.user_choice == 1:
                self.sort_emp("Name", self.the_employee_list)

            elif self.user_choice == 2:
                self.sort_emp("Level", self.the_employee_list)
                
            elif self.user_choice == 3:
                self.sort_emp("Job Position", self.the_employee_list)
                
            elif self.user_choice == 4:
                self.sort_emp("Date Hired", self.the_employee_list)
                
            elif self.user_choice == 5:
                self.sort_emp("Pay", self.the_employee_list)

            elif self.user_choice == 6:
                self.sort_emp("Date Departed", self.the_employee_list)

            elif self.user_choice == 7:
                self.display_main_menu()
            else:
                print("Please input an integer from 1-7.")
                self.display_sort_menu()

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
                7) Cancel sort
            """
        )

class Take_input:
    def __init__(self, input_type, input_disp_text):
        self.input_type = input_type
        self.input_disp_text = input_disp_text
        self.the_user_input = None
        self.take_input()

    def take_input(self):
        if self.input_type == "int":
            while True:
                try:
                    user_input = int(input(self.input_disp_text + ": "))
                    if user_input is not None:
                        break
                except:
                    print("Please try again.")

            self.the_user_input = user_input
            return
        
        elif self.input_type == "string":
            while True:
                try:
                    user_input = str(input(self.input_disp_text + ": "))
                    if user_input is not None:
                        break
                except:
                    print("Please try again.")

            self.the_user_input = user_input
            return

        elif self.input_type == "money":
            while True:
                try:
                    user_input = int(input(self.input_disp_text + ": $"))
                    if user_input is not None:
                        break
                except:
                    print("Please try again.")

            user_input = f'{user_input:,}'
            user_input = "$" + str(user_input)

            self.the_user_input = user_input
            return

        elif self.input_type == "verify":
            possible_values = ["Y", "N", "y", "n"]
            while True:
                try:
                    user_input = str(input(self.input_disp_text + " (Y/N): "))
                    if user_input is not None and user_input in possible_values:
                        break
                except:
                    print("Please try again.")

            self.the_user_input = user_input
            return

#TODO:
'''

    **MAIN THING**
    REWIRE ALL OF THE REDIRECTS!!!

    Make application super class and everything else sub of application
'''

employee_lists = EmployeeList()
the_employees_cur = employee_lists.employee_list_cur
the_employees_dep = employee_lists.employee_list_dep

the_menu = Menu()
the_menu.run()
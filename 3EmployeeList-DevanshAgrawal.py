import csv, sys
from operator import itemgetter

class EmployeeList():
    def __init__(self, employee_list):
        self.employee_list = employee_list
        self.employee_list_cur = []
        self.employee_list_dep = []

    def sort_emp(self, sort_key, the_employee_list):
        temp_emp_list = the_employee_list
        if len(temp_emp_list) > 0:
            temp_emp_list.sort(key=itemgetter(sort_key))

        employee_displayer = Employee(temp_emp_list)

        employee_displayer.display_emp(temp_emp_list)
        input("Press ENTER")
        self.display_main_menu()

    def search_emp(self, search_name):
        for emp in self.employee_list:
            if emp['Name'] == search_name:
                return emp

    def add_emp(self):
        print("Please input the following information about the new employee:")
        
        while True:
            new_name = TakeInput("string", "Name").the_user_input
            searcher = EmployeeList(self.employee_list)
            emp_data = searcher.search_emp(new_name)
            if emp_data is not None and not emp_data['Date Departed']:
                print("This employee already exists. Please try again.")
            else:
                break

        new_level = TakeInput("string", "Level").the_user_input

        new_month = TakeInput("int", "Month (MM)").the_user_input
        #fills the number in with zeros
        new_month = f'{new_month:02}'

        new_day = TakeInput("int", "Day (DD)").the_user_input
        #fills the number in with zeros
        new_day = f'{new_day:02}'

        while True:
            new_year = TakeInput("int", "Year (YYYY)").the_user_input
            if len(str(new_year)) == 4:
                break
            else:
                print("Please input four integers.")

        new_pay = TakeInput("money", "Pay").the_user_input
        new_pay = str(new_pay)

        new_position = TakeInput("string", "Position").the_user_input

        new_date = str(str(new_year)+"-"+str(new_month)+"-"+str(new_day))

        final_input = TakeInput("verify", "Are you sure you want to add this new employee?").the_user_input

        if final_input == "y" or final_input == "Y":
            self.employee_list.append({
                "Name": new_name,
                "Level": new_level,
                "Date Hired": new_date,
                "Pay": new_pay,
                "Job Position": new_position,
                "Date Departed": ''
            })
            print("This employee has been added to the system.")
            input("Press ENTER")
        else:
            print("You will now be redirected to the main menu.")

        return

    def delete_emp(self):
        while True:
            the_user_input = TakeInput("string", "What is the name of this employee?").the_user_input
            searcher = EmployeeList(self.employee_list)
            emp_data = searcher.search_emp(the_user_input)

            employee_index = None
            for index in range(len(self.employee_list)):
                if self.employee_list[index] == emp_data:
                    print("Found a Match!")
                    if self.employee_list[index]['Date Departed']:
                        print("This employee is already retired.")
                        employee_redirect = TakeInput("verify",
                            '''
                            Input "Y" if you want to go back to the main menu
                            Input "N" if you want to try deleting another employee.
                            '''
                        ).the_user_input
                        if employee_redirect == "Y" or employee_redirect == "y":
                            return
                    else:
                        employee_index = index

            if employee_index:
                break
            else:
                print("This employee does not exist in the system. Please try again.")

        while True:
            departed_year = TakeInput("int", "What year did the employee depart? (YYYY)").the_user_input
            if len(str(departed_year)) == 4:
                break
            else:
                print("Please input four integers.")

        departed_month = TakeInput("int", "what month did the employee depart?").the_user_input
        departed_month = f'{departed_month:02}'

        departed_day = TakeInput("int", "what day of the month did the employee depart?").the_user_input
        departed_day = f'{departed_day:02}'

        final_date = str(str(departed_year)+"-"+str(departed_month)+"-"+str(departed_day))

        final_choice = TakeInput("verify", "Are you sure you want to delete this employee?").the_user_input

        if final_choice == "Y" or final_choice == "y":
            self.employee_list[employee_index]['Date Departed'] = final_date
            print("Employee deleted.")
            input("Press ENTER")
        else:
            print("You will now be redirected to the main menu.")

class Employee():
    def __init__(self, the_employee_list):
        self.the_employee_list = the_employee_list
        print(self.the_employee_list)
        #Name, Level, Date, Pay, Position, Departed
        self.max_lengths = [0, 0, 0, 0, 0, 0]
        
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
        for emp in self.the_employee_list:
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

    def get_max_lengths(self):
        for row in self.the_employee_list:
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
        final_input = TakeInput("verify", "Are you sure you want to save the file?")
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
        self.file_object = File(self.employee_list)
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
        self.file_object.file_reader()
        self.employee_list = self.file_object.the_employee_list

        while self.done == False:
            self.display_main_menu()

            possible_choices = [1, 2, 3, 4, 5, 6, 7]
            input_valid = False

            self.user_choice = TakeInput("int", "Insert Choice").the_user_input
            self.redirect_user()

    def redirect_user(self):
        if self.user_choice != 3:
            print(self.employee_list)
            employee_options = Employee(self.employee_list)
            employee_list_interactions = EmployeeList(self.employee_list)
            if self.user_choice == 1:
                employee_list_interactions.add_emp()
                #updates the employee list with added emp.
                self.employee_list = employee_list_interactions.employee_list

            elif self.user_choice == 2:
                employee_list_interactions.delete_emp()
                self.employee_list = employee_list_interactions.employee_list

            elif self.user_choice == 3:
                self.display_sort_menu()
                the_user_input = TakeInput("int", "Insert choice").the_user_input
                self.redirect_user_sort(the_user_input)
                
            elif self.user_choice == 4:
                searching_name = TakeInput("string", "What is the name of this employee?").the_user_input
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
                employee_options.display_emp()
            
            elif self.user_choice == 7:
                print("Have a nice day.")
                sys.exit()

        elif self.user_choice == 3:
            self.display_sort_menu()
            self.user_choice = TakeInput("int", "Insert Choice").the_user_input
            employee_sorter = EmployeeList()

            if self.user_choice == 1:
                employee_sorter.sort_emp("Name", self.employee_list)

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

class TakeInput:
    def __init__(self, input_type, input_disp_text):
        self.input_type = input_type
        self.input_disp_text = input_disp_text
        self.the_user_input = None
        self.take_input()

    def take_input(self):
        input_valid = False
        if self.input_type == "int":
            while input_valid is False:
                try:
                    user_input = int(input(self.input_disp_text + ": "))
                    if user_input is not None:
                        input_valid = True
                except:
                    print("Please try again.")

            self.the_user_input = user_input
            return
        
        elif self.input_type == "string":
            while input_valid is False:
                try:
                    user_input = str(input(self.input_disp_text + ": "))
                    if user_input is not None:
                        break
                except:
                    print("Please try again.")

            self.the_user_input = user_input
            return

        elif self.input_type == "money":
            while input_valid is False:
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
            while input_valid is False:
                try:
                    user_input = str(input(self.input_disp_text + " (Y/N): "))
                    if user_input is not None and user_input in possible_values:
                        break
                except:
                    print("Please try again.")

            self.the_user_input = user_input
            return

        elif self.input_type == "menu":
            possible_values = [1, 2, 3, 4, 5, 6, 7]
            while input_valid is False:
                try:
                    user_input = int(input(self.input_disp_text + ": "))
                    if user_input is not None and user_input in possible_values:
                        input_valid = True
                except:
                    print("Please input and integer from 1-7.")

#TODO:

'''

    **MAIN THING**
    REWIRE ALL OF THE REDIRECTS!!!

    Make application super class and everything else sub of application
'''

'''
employee_lists = EmployeeList()
the_employees_cur = employee_lists.employee_list_cur
the_employees_dep = employee_lists.employee_list_dep
'''
the_menu = Menu()
the_menu.run()
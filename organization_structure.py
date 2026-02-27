class Individual:
    def __init__(self, person_name, person_age):
        self.person_name = person_name
        self.person_age = person_age

    def display_info(self):
        print(f"Name: {self.person_name}, Age: {self.person_age}")

class Staff(Individual):
    def __init__(self, person_name, person_age, staff_code, pay):
        super().__init__(person_name, person_age)
        self.staff_code = staff_code
        self.pay = pay

    def display_info(self):
        super().display_info()
        print(f"Staff Code: {self.staff_code}, Salary: {self.pay:.2f}")

class Supervisor(Staff):
    def __init__(self, person_name, person_age, staff_code, pay, section):
        super().__init__(person_name, person_age, staff_code, pay)
        self.section = section

    def display_info(self):
        super().display_info()
        print(f"Section: {self.section}")

if __name__ == "__main__":
    while True:
        print("\nMenu Options:")
        print("1 - Add Individual")
        print("2 - Add Staff")
        print("3 - Add Supervisor")
        print("4 - Quit")

        option = input("Select option: ")

        if option == "1":
            nm = input("Enter name: ")
            ag = int(input("Enter age: "))
            obj = Individual(nm, ag)
            obj.display_info()

        elif option == "2":
            nm = input("Enter name: ")
            ag = int(input("Enter age: "))
            code = input("Enter staff code: ")
            salary_amt = float(input("Enter salary: "))
            obj = Staff(nm, ag, code, salary_amt)
            obj.display_info()

        elif option == "3":
            nm = input("Enter name: ")
            ag = int(input("Enter age: "))
            code = input("Enter staff code: ")
            salary_amt = float(input("Enter salary: "))
            dept = input("Enter section: ")
            obj = Supervisor(nm, ag, code, salary_amt, dept)
            obj.display_info()

        elif option == "4":
            print("Program terminated.")
            break

        else:
            print("Invalid input. Try again.")
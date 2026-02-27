class Vehicle:
    def __init__(self, make, variant, manufacture_year):
        self.make = make
        self.variant = variant
        self.manufacture_year = manufacture_year

    def show_details(self):
        print(f"{self.make} {self.variant} ({self.manufacture_year})")

v1 = Vehicle("Toyota", "Supra", 2019)
v2 = Vehicle("BMW", "M4", 2022)

v1.show_details()
v2.show_details()
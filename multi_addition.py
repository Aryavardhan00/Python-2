class Adder:
    def add_numbers(self, a=0, b=0, c=0):
        return a + b + c

calc_obj = Adder()

print(calc_obj.add_numbers(2))
print(calc_obj.add_numbers(2, 3))
print(calc_obj.add_numbers(2, 3, 4))
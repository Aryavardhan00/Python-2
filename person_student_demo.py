class Human:
    def __init__(self, full_name, years):
        self.full_name = full_name
        self.years = years

    def show_profile(self):
        print(self.full_name, self.years)

class Learner(Human):
    def __init__(self, full_name, years, score):
        super().__init__(full_name, years)
        self.score = score

    def introduce(self):
        print("Hello, I am currently studying.")

student_obj = Learner("Rohit", 19, 88)
student_obj.introduce()

student_obj.score = 91
student_obj.full_name = "Aditya"

student_obj.show_profile()
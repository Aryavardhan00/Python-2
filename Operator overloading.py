class Package:
    def __init__(self, mass):
        self.mass = mass

    def __add__(self, other):
        return self.mass + other.mass

pkg1 = Package(12)
pkg2 = Package(18)

print(pkg1 + pkg2)

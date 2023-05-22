class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def scream(self, level):
        self.level = level
        print('you are screaming ', self.level)


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.scream('Super loud')

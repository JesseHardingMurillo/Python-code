class person:
    # Add attributes to the class or characteristics
    # __  = dunder = double underscore
    # method constructor
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age


# Ask for data
name = input("Enter the name: ")
lastname = input("Enter the lastname: ")
age = int(input("Enter the age: "))

# Create objet
person1 = person(name, lastname, age)
print(person1.name)
print(person1.lastname)
print(person1.age)

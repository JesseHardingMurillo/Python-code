class person:
    # Add attributes to the class or characteristics
    # __  = dunder = double underscore
    # method constructor
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

# Create objet
# First object
person1 = person('Juan', 'Perez', 28)
print(f'Object person 1: {person1.name} {person1.lastname} {person1.age}')
# Second object
person2 = person('Karla', 'Gomez', 30)
print(f'Object person 1: {person2.name} {person2.lastname} {person2.age}')

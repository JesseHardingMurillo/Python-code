class person:
    # Add attributes to the class or characteristics
    # __  = dunder = double underscore
    # method constructor
    # self == this but documentation recommend only use self

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    # method
    def showDetail(self):
        print(f'Person: {self.name} {self.lastname}, age: {self.age}.')


# Create objet
# First object
person1 = person('Juan', 'Perez', 28)
person1.showDetail()
# Second object
person2 = person('Karla', 'Gomez', 30)
person2.showDetail()
# print(f'Object person 1: {person2.name} {person2.lastname} {person2.age}')

person.showDetail(person1)

# add new attribute but not share with the second objetc
person1.telephone = ' 83235555'
print(person1.telephone)

# print(person2.telephone)
# AttributeError: 'person' object has no attribute 'telephone'

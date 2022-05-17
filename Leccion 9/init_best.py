class person:
    # Add attributes to the class or characteristics
    # __  = dunder = double underscore
    # method constructor
    # past tuple of values = *args
    # past list of dictionary = **kwargs
    def __init__(self, name, lastname, age, *values, **terms):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.values = values
        self.terms = terms

    def showDetail(self):
        print(f'Person: {self.name} {self.lastname}, age: {self.age}. numbers : {self.values}, fruits: {self.terms}')


person1 = person('Juan', 'Perez', 28, "5555555", 2, 3, 4, a="apple", pear="pear")
person1.showDetail()
# Second object
person2 = person('Karla', 'Gomez', 30)
person2.showDetail()

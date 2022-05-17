class person:
    # Add attributes to the class or characteristics
    # __  = dunder = double underscore
    # method constructor

    def __init__(self, name, lastname, age):
        # self._name =name  <-- the _ indicate to only this class can access but if I crete other object like car,
        # that class can't access to attribute name of the class person
        self.__name = name
        self.lastname = lastname
        self.age = age

    def showDetail(self):
        print(f'Person: {self.__name} {self.lastname}, age: {self.age}')


person1 = person('Juan', 'Perez', 28)
# I shouldn't do this, but I can, but it is not recommended :
# person1._name = "Pepe"
# Because I am out of the class
# But if I use dunder I can change the attribute
person.__name = 'Pepe'
person1.showDetail()


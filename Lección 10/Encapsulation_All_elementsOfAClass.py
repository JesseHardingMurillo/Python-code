class person:

    def __init__(self, name, lastname, age):
        self._name = name #<--The underscore is for encapsulation
        self._lastname = lastname #<--
        self._age = age #<--
    
    # Get method
    # Decorators modify the behavior of our method
    @property  # <-- Decorators
    def name(self):
        print("Calling method get")
        return self._name

    @property
    def lastname (self):
        return self._lastname

    @property
    def age (self):
        return self._age

    @name.setter
    def name(self, name):
        print("Calling method set")
        print("The name has been successfully changed ")
        self._name = name

    @lastname.setter
    def lastname (self, lastname):
        print("Calling method set")
        print("The lastname has been successfully changed ")
        self._lastname = lastname

    @age.setter
    def age (self, age):
        print("Calling method set")
        print("The age has been successfully changed ")
        self._age = age

    def showDetail(self):
        print(f'Person: {self._name} {self._lastname}, age: {self._age}')

    #Method for delete an object
    def __del__ (self):
        print(f'Person: {self._name} {self._lastname} has been delete')

#So that it is only executed in this file and not in another that the classes and methods are being imported
if __name__ == "__main__":
    person1 = person('Juan', 'Perez', 28)
    person1.name = 'Juan Carlos'
    print(person1.name)
    person1.lastname = "Lara"
    person1.age = 30
    person1.showDetail()

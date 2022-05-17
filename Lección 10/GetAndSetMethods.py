class person:

    def __init__(self, name, lastname, age):
        self._name = name
        self.lastname = lastname
        self.age = age

    # Get method
    # Decorators modify the behavior of our method
    @property  # <-- Decorators
    def name(self):
        print("Calling method get")
        return self._name

    @name.setter
    def name(self, name):
        print("Calling method set")
        print("The name has been successfully changed ")
        self._name = name

    def showDetail(self):
        print(f'Person: {self._name} {self.lastname}, age: {self.age}')


person1 = person('Juan', 'Perez', 28)
print(person1.name)
person1.name = 'Juan Carlos'
print(person1.name)

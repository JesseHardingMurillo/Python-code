# Father class
class person:
    def __init__(self, name, lastname, age):
        self.name = name 
        self.lastname = lastname 
        self.age = age

    def __str__(self) -> str:
        return f"Person: {self.name} {self.lastname}, age: {self.age}"
    
#Son class
class employee(person):
    def __init__(self, name, lastname, age, salary):
        super().__init__(name, lastname, age)
        self.salary = salary

    def __str__(self) -> str:
        #For inheritance the method str the father class from son class
        return f"{super().__str__()}, salary: ${self.salary}"
    

employee1=employee("Jesse", "Harding","19","10000")




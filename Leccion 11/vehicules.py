class vehicules():
    def __init__(self,brand ,n_passengers,n_wheels, color) :
         self.brand = brand
         self.n_passengers = n_passengers
         self.n_wheels= n_wheels
         self.color = color
    def __str__(self):
        return f"""
        Brand: {self.brand}
        Number of passengers: {self.n_passengers}
        Number of wheels: {self.n_wheels}
        """

class cars (vehicules):
    def __init__(self, brand, n_passengers, n_wheels, model, year,color, speed ):
        super().__init__(brand, n_passengers, n_wheels,color)
        self.model = model
        self.year = year
        self. speed =speed

    def __str__(self):
        #For inheritance the method str the father class from son class
        return f"""
        {super().__str__()}Model: {self.model}
        Year: {self.year}
        Speed: {self.speed}"""

class bikes (vehicules):
    def __init__(self, brand, n_passengers, n_wheels, color, accessories, type_b):
        super().__init__(brand, n_passengers, n_wheels, color)
        self.accersories = accessories
        self.type_b = type_b

    def __str__(self) -> str:
        #For inheritance the method str the father class from son class
        return f"""
        {super().__str__()}Accersories : {self.accersories}
        Type: {self.type_b}"""
    

car1 = cars("Toyota", 5, 4 , "Tacoma", 2020 , "Black", "120Km/h")
bike1 =bikes("Trek", 1 , 2 ,"Wine",["Helmet", "Pedals"], "Urban" )
print(car1)
print(bike1)

#Theacher example 
# class Vehiculo():    
#     def __init__(self, color, ruedas):
#         self.color = color
#         self.ruedas = ruedas

#     def __str__(self):
#         return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)

# class Coche(Vehiculo):
#     def __init__(self, color, ruedas, velocidad):
#         super().__init__(color, ruedas)
#         self.velocidad = velocidad

#     def __str__(self):
#         return super().__str__() + ", Velocidad (km/hr): " + str(self.velocidad)
    
# class Bicicleta(Vehiculo):
#     def __init__(self, color, ruedas, tipo):
#         super().__init__(color, ruedas)
#         self.tipo = tipo

#     def __str__(self):
#         return super().__str__() + ", Tipo: " + self.tipo
    
# vehiculo = Vehiculo("Rojo", 4)
# print(vehiculo)

# coche = Coche("Azul", 4, 150)
# print(coche)

# bicicleta = Bicicleta("Blanca", 2, "Urbana")
# print(bicicleta)   
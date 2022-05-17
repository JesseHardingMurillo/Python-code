print("Proporcione los siguientes datos del libro")
nombre = input("Proporcione el nombre: ")
id = (input("Proporcione el ID: "))
price = float(input("Proporcione el precio: "))
gratis = input("Indica si el envio es gratis (True/False): ")
if gratis == "True":
    gratis = True
elif gratis == "False":
    gratis = False
else:
    print("Solo debe digitar True or False")
print(f"Nombre': {nombre}")
print(f"ID: {id}")
print(f"Precio:{price}")
if gratis:
    print(f"Envio gratuito: Sí")
else:
    print(f"Envio gratuito: No")
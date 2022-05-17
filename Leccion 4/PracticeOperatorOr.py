vaciones = False
diaDescanso = False

data = input("Tiene libre para el dia del"
             "- partido (respuesta si/no): ")

if data == "si":
    que = input("¿vacaciones o descanso?: ")
    if que == "vacaciones":
        vaciones = True
    elif que == "descanso":
        diaDescanso = True

if vaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("Tiene deberes que hacer ")
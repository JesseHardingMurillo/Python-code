nota = float(input("Proporcione un valor entre 0 y 10: "))
calificacion = None
if 10 >= nota >= 9:
    calificacion = "A"
elif 9 > nota >= 8:
    calificacion = "B"
elif 8 > nota >= 7:
    calificacion = "C"
elif 7 > nota >= 6:
    calificacion = "D"
elif 6 > nota >= 0:
    calificacion = "F"
else:
    calificacion = "Valor desconocido"

print(f'La nota {nota} hace referencia a una calificacion de {calificacion}')



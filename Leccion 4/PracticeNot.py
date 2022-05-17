vacaciones = False
diaDescanso = False
# Si es True lo convierte en False y si es False lo convierte en True
if not (vacaciones or diaDescanso):
    print("Tiene deberes que hacer")
else:
    print("Tiene vacaciones")
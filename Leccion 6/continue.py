#Determinar cuales numeros son ceros desde un numer
# for j in range(6):
#     if j % 2 == 0:
#         print(f"Value: {j}")

for j in range(6):
    #Check if it is odd so as not to print in console
    if j % 2 != 0:
        continue
    print(f'Value: {j}')



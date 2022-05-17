# Valor between 0 and 5

number = int(input("Write a number: "))

valorMinim = 0
valorMax = 5

InRange = number >= valorMinim and number <= valorMax

if InRange:
    print(f'The number {number} is the range')
else:
    print(f"The number {number} isn't the range")


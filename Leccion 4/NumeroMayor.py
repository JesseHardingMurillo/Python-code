
try:
    number1 = int(input("Enter the number 1: "))
    number2 = int(input("Enter the number 2: "))

    if number1 > number2:
        print(f'The greater number is:{number1}')
    elif number1 == number2:
        print('Have the same value')
    else:
        print(f'The greater number is:{number2}')
except ValueError:
    print("Entered an invalid character")



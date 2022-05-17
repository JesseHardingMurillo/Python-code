def celsius_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# menu
print("""
1- Celsius to fahrenheit
2- Fahrenheit to celsius""")

print("---------------------------")
option = int(input("Enter the required option: "))

if option == 1:
    temperature = int(input("Enter the temperature in degrees celsius: "))
    print(f'The temperature is the {celsius_fahrenheit(temperature)}°F')
else:
    temperature = int(input("Enter the temperature in degrees fahrenheit: "))
    print(f'The temperature is the {fahrenheit_celsius(temperature)}°C')

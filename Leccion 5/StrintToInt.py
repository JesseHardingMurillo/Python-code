number = int(input("Enter a number between 1 and 3:  "))
name = ""
if number == 1:
    name = "one"

elif number == 2:
    name = "two"

elif number == 3:
    name = "three"

else:
    name = "You enter a invalid character or number"

print(f'The number: {number} - {name}')
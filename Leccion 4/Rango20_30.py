age = int(input("Introduce your age: "))

# twenty = age >= 20 and age < 30
# print(twenty)
#
# thirty = age >= 30 and age < 40
# print(thirty)

if (age >= 20 and age < 30) or (30 and age < 40):
    if (age >= 20 and age < 30):
        print("You are in the range of (20's)")
    elif (30 and age < 40):
        print("You are in the range of (30's)")

else:
    print("You aren't in the range of (20's) or (30's)")
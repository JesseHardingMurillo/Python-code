# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
# Determine a factorial
def factorail(number):
    if number == 1:
        return 1
    else:
        # Repeat again de function factorial
        return number * factorail(number - 1)


result = factorail(5)

print(f'The factorial of 5 is {result}')

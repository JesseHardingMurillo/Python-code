def multiply(*numbers):
    result = 1
    for n in numbers:
        result = n * result
    return result

print(multiply(3, 5, 15))

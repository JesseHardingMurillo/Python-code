def addition(*numbers) -> int:
    result = 0
    for n in numbers:
        result += n
    return result


print(addition(4, 3, 5, 6))

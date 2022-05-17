def counting(number):
    if number >= 1:
        print(number)
        counting((number - 1))


counting(5)

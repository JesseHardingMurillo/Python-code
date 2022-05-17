class rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return f'The area of rectangle is {self.base * self.height}'


base = float(input('Enter value of the base: '))
height = float(input('Enter value of the height: '))
rectangle1 = rectangle(base, height)
print(rectangle1.area())

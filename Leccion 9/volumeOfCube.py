class cube:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return f'The volume of cube is {self.width * self.height * self.depth}'


width = float(input('Enter value of the width: '))
height = float(input('Enter value of the height: '))
depth = float(input('Enter value of the depth: '))
cube1 = cube(width, height , depth)
print(cube1.volume())

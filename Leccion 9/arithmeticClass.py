class arithmetic:
    """
    class arithmetic for do operation to plus,subtraction , division, etc.
    """

    def __init__(self, operatorA, operatorB):
        self.operatorA = operatorA
        self.operatorB = operatorB

    def plus(self):
        return self.operatorA + self.operatorB

    def subtraction(self):
        return self.operatorA - self.operatorB

    def multiply(self):
        return self.operatorA * self.operatorB

    def division(self):
        return self.operatorA / self.operatorB

arithmetic1 = arithmetic(5, 3)
print(f'Plus: {arithmetic1.plus()}')
print(f'Subtraction: {arithmetic1.subtraction()}')
print(f'Multiply: {arithmetic1.multiply()}')
# :.3f is to indicate the decimals 
print(f'Division : {arithmetic1.division():.3f}')

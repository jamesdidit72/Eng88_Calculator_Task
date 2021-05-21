# Calculator

class Calculator:
    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def add(self, value_1, value_2):
        return value_1 + value_2

    def subtract(self, value_1, value_2):
        return value_1 - value_2

    def multiply(self, value_1, value_2):
        return value_1 * value_2

    def divide(self, value_1, value_2):
        return value_1 / value_2

    def method(self, value_1, value_2):
        if value_2 == 0:
            return False
        elif value_1 % value_2 == 0:
            return True
        else:
            return False

    def triangle(self, height, base):
        return (height * base) / 2

    def inch(self, value_1):
        return value_1 * 2.54


mycalc = Calculator(5, 5)

print(mycalc.add(5, 5))
print(mycalc.subtract(5, 5))
print(mycalc.multiply(5, 5))
print(mycalc.divide(5, 5))
print(mycalc.method(5, 5))
print(mycalc.triangle(5, 5))
print(mycalc.inch(5))

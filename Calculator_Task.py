# Calculator

class Calculator:  # initialisation of the class
    def __init__(self, value_1, value_2):  # function that sets the values
        self.value_1 = value_1
        self.value_2 = value_2

    def add(self, value_1, value_2):  # add function
        return value_1 + value_2

    def subtract(self, value_1, value_2):  # subtract function
        return value_1 - value_2

    def multiply(self, value_1, value_2):  # multiply function
        return value_1 * value_2

    def divide(self, value_1, value_2):  # divide function
        return value_1 / value_2

    def method(self, value_1, value_2):  # divisible function
        if value_2 == 0:
            return False
        elif value_1 % value_2 == 0:  # if the value_1 can be divided by the value_2 with no remainder, then return True
            return True
        else:
            return False

    def triangle(self, height, base):  # area of a triangle function
        return (height * base) / 2

    def inch(self, value_1):
        return value_1 * 2.54  # multiplies the value by the length of an inch in centimeters


mycalc = Calculator(5, 5)

print(mycalc.add(5, 5)) # calls the class and sets the variables to 5
print(mycalc.subtract(5, 5))
print(mycalc.multiply(5, 5))
print(mycalc.divide(5, 5))
print(mycalc.method(5, 5))
print(mycalc.triangle(5, 5))
print(mycalc.inch(5))  # calls the class and sets the variable to 5

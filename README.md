# Object Oriented Calculator
## Build a basic object Orientated Calculator
### phase 1: 
- build a simple calculator class containing add, subtract, multiply, divide.
### phase 2: expand by creating:
- Divisible by method that returns true or false dependent on the outcome
- Work out and return the area of a triangle
- inch to cm converter
#### NOTE -> Must be in class and method format

### Phase 1:
```python
# Calculator
class calculator:
    @staticmethod
    def add(value_1, value_2):
        return value_1 + value_2

    def subtract(value_1, value_2):
        return value_1 - value_2

    def multiply(value_1, value_2):
        return value_1 * value_2

    def divide(value_1, value_2):
        return value_1 / value_2


print(calculator.add(5, 5))
print(calculator.subtract(5, 5))
print(calculator.multiply(5, 5))
print(calculator.divide(5, 5))

```
### Phase 2:
```python
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

```

### Comments
```python
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

```
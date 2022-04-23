""" This is a calculator program.
    It takes a string of operations and numbers and returns the result.
    It can also use parentheses to change the order of operations.
"""
# A class that takes a string of operations and numbers and returns the result.
class Calculator:
    def __init__(self, string):
        self.string = string
        self.operations = {'+': self.add, '-': self.subtract, '*': self.multiply, '/': self.divide, '^': self.power}
        self.numbers = []
        self.operators = []
        self.result = 0

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def power(self, num1, num2):
        return num1 ** num2

    def evaluate(self):
        # Split the string into numbers and operators.
        for i in self.string:
            if i.isdigit():
                self.numbers.append(int(i))
            elif i in self.operations:
                self.operators.append(i)
        # Evaluate the numbers and operators.
        while self.operators:
            operator = self.operators.pop(0)
            num1 = self.numbers.pop(0)
            num2 = self.numbers.pop(0)
            self.result = self.operations[operator](num1, num2)
            self.numbers.insert(0, self.result)
        return self.result

def main():
    while True:
        string = input('Enter an operation: ')
        if string == 'quit':
            break
        else:
            calc = Calculator(string)
            print(calc.evaluate())
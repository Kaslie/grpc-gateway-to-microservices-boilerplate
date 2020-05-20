
class Calculator(object):
    @classmethod
    def add(cls, a, b):
        return int(a + b)

    @classmethod
    def multiply(cls, a, b):
        return int(a * b)

    @classmethod
    def subtract(cls, a, b):
        return int(a - b)

    @classmethod
    def division(cls, a, b):
        return int(a / b)
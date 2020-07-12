from decimal import *
import string


def my_judg(a):
    if str(a).isdigit():
        return str(a)
    else:
        return str(a.quantize(Decimal('0.00')))


class Calculator:
    def add(self, a, b):
        result = Decimal(str(a)) + Decimal(str(b))
        return my_judg(result)

    def div(self, a, b):
        result = Decimal(str(a)) / Decimal(str(b))
        return my_judg(result)

    def sub(self, a, b):
        result = Decimal(str(a)) - Decimal(str(b))
        return my_judg(result)

    def mul(self, a, b):
        result = Decimal(str(a)) * Decimal(str(b))
        return my_judg(result)


if __name__ == '__main__':
    c = Calculator()
    print(c.add(0.556, 0.3), c.div(10, 3), c.sub(5.5, 8.9), c.sul(3.33, 1.2))

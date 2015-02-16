#Find e to the Nth Digit
# Using Taylor Series http://en.wikipedia.org/wiki/Taylor_series

import math
import decimal
D = decimal.Decimal
limit = 26

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

def calcE(percision):
    e = D(2)
    count = 2
    while count < 26:
        # print(count)
        e += D(1)/factorial(D(count))
        # print(e)
        count += 1

    e_digits = format(e,'.%sf'%(percision))

    return e_digits


def main():
    e_digits = calcE(int(input(
        "Enter the number of decimals to calculate to: ")))

    print e_digits

if __name__ == '__main__':
    main()
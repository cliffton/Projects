#!/usr/bin/python

#Python 2.7.9
# Machin-like formula for calculating pi ( Uses invert trigo )
# TODO:- Limit for percision

"""
pi/4 = [ 4 x arctan(1/5) ] - [ arctan(1/239) ] 

"""

import decimal
import math
D = decimal.Decimal
four = D(4)
onebyfive = D(1)/D(5)
oneby239 = D(1)/D(239)


def calcPi(pi_digits):
    pi = four * ( four * D(math.atan(onebyfive))  -  D(math.atan(oneby239)) )
    pi_digits = format(pi,'.%sf'%(pi_digits))
    return pi_digits


def main():
    pi_digits = calcPi(int(input(
        "Enter the number of decimals to calculate to: ")))

    print pi_digits

if __name__ == '__main__':
    main()    
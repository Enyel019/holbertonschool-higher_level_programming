#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lnumber = number%10
if lnumber > 5:
    print('Last digit of {:d} is {:d} and is greater than {:d}'.format(number,lnumber,5))
elif lnumber == 0:
    print('Last digit of {:d} is {:d} and is {:d}'.format(number,lnumber,0))
elif lnumber < 6 and lnumber != 0:
    print('Last digit of {:d} is {:d} and is less than {:d} and not {:d}'.format(number,lnumber,5,0))

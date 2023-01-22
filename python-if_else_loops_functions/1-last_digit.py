#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if ld == 0:
    print("Last digit of {:d} is {:d} and is {:d}".format(number, ld, 0))
if ld > 5:
    print("Las digit of {:d} is {:d} and is gradter than {:d}"
          .format(number, ld, 5))
if ld < 6 and ld != 0:
    print("Las digit of {:d} is {:d} and is less than {:d} and not {:d}"
          .format(number, ld, 6, 0))

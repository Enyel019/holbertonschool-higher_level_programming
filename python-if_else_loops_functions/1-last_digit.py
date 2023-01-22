#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")
if ld > 5:
    print(f"Las digit of {number} is {ld} and is gradter than 5")
if ld < 6 and ld != 0:
    print(f"Las digit of {number} is {ld} and is than 6 and not 0")

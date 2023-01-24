#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        print('{:s}'.format(chr(i)), end="")
    elif i % 2 != 0:
        print('{:s}'.format(chr(i - 32)), end="")

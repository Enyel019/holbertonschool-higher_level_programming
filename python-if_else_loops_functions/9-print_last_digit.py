#!/usr/bin/python3
def print_last_digit(number):
        if number < 0:
                r = ((number * -1) % 10)
                print('{:d}'.format(r), end="")
                return r
        else:
                print('{:d}'.format(number % 10), end="")
                return number % 10

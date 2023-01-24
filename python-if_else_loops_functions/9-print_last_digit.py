#!/usr/bin/python3
def print_last_digit(number):
        if number < 0:
                result = ((number * -1) % 10)
                print('{:d}'.format(result), end="")
                return result
        else:
                print('{:d}'.format(number % 10), end="")
                return number % 10

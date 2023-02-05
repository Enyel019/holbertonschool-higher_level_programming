#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as tool:
        print("Exception: {:s}".format(str(tool)), file=sys.stderr)
        return False

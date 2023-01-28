#!/usr/bin/python3
if __name__ == "__main__":
    add = 0
    import sys
    for i in range(1, len(sys.argv)):
        add += int(sys.argv[i])
    print("{:d}".format(add))

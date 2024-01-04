#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    number = len(argv) - 1
    if number == 0:
        print("0 arguments.")
    else:
        print("{} argument:".format(number))
        for i in range(number):
            print("{}: {}".format((i + 1), argv[i + 1]))

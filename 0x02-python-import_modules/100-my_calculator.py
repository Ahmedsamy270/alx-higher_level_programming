#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import mul, div, sub, add
    from sys import argv
    lenth = len(argv) - 1
    a = int(argv[1])
    b = int(argv[3])
    res = a + b
    for i in range(lenth + 1):
        if lenth < 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            print("1")
        elif argv[2] != '+' or argv[2] != '-' or argv[2] != '*' or argv[2] != '/+':
            print("Unknown operator. Available operators: +, -, * and /")
            print("1")
        else:
            print("{} + {} = {}".format(a, b, res))


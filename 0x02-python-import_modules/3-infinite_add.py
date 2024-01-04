#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    total = 0
    lenth = len(argv) - 1
    if lenth == 0:
        print("0")
    else:
        for i in range(lenth):
            total += int(argv[i + 1])
        print("{}".format(total))

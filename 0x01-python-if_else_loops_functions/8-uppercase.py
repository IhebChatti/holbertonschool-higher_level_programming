#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            c = ord(i) - 32
        print("{}".format(chr(c)), end='')
    print("")

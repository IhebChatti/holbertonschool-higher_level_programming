#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print('0 arguments')
elif len(sys.argv) == 2:
    print('{} argument:'.format(len(sys.argv)-1))
    for i in range (1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
else:
    print('{} arguments:'.format(len(sys.argv)-1))
    for i in range (1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
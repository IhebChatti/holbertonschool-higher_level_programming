#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = n % 10
if ld > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, ld))
elif l == 0:
    print('Last digit of {} is {} and is 0'.format(number, ld))
elif l < 6:
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, ld))
else:
    pass

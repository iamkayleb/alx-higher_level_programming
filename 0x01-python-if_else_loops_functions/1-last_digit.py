#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last_digit = number[-1]
n = int(last_digit)

if number.startswith('-'):
    n = n * -1
if n > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, n))
elif n < 6 and last_digit != 0:
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, n))
else:
    print('Last digit of {} is {} and is 0'.format(number, n))

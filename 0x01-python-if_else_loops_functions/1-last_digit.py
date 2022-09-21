#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = abs(number)
x = [int(a) for a in str(num2)]
x = x[-1]
if number < 0:
    y = -abs(x)
else:
    y = x
if y > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, y))
elif y == 0:
    print("Last digit of {} is {} and is 0".format(number, y))
elif y < 6 and y != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format
          (number, y))

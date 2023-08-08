#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_num_str = number_str[-1]
last_num = int(last_num_str)
if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num < 6 and last_num != 0:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_num} and is 0")


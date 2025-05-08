#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

final_digit = abs(number) % 10

if number > 5:
    print(f"Last digit of", number, "is", final_digit, "and is greater than 5", "\n")

elif number < 6 > 0:
    print(f"Last digit of", number, "is", final_digit, "and is less than 6 and not 0", "\n")

elif number == 0: 
    print(f"Last digit of", number, "is", final_digit % 10, "and is 0", "\n")

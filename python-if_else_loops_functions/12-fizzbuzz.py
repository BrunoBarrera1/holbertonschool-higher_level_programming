#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 99):
        if number % 3 == 0 and number % 5 == 0:
            print((number),"FizzBuzz ")
        elif number % 3 == 0:
            print((number),"Fizz ")
        elif number % 5 == 0:
            print((number),"Buzz ")

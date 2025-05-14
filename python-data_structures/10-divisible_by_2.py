#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bruno = []
    for number in my_list:
        bruno.append(number % 2 == 0)
    return bruno

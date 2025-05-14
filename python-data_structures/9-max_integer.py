#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    bruno = my_list[0]
    for num in my_list:
        if num > bruno:
            bruno = num
    return bruno

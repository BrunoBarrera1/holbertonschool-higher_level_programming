#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for item in my_list:
        if type(item) != int:
            raise TypeError("All elements must be integers")
        print("{:d}".format(item))

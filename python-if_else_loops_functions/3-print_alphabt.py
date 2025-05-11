#!/usr/bin/python3
no = "e"
no1 = "q"
for juan in range (97, 123):
    character = chr(juan)
    if juan != no and juan != no1:
        print(juan, end="".format(juan))

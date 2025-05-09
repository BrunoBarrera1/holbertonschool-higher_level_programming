#!/usr/bin/python3
for juan in range (97, 123):

    if juan not in (ord('q'), ord('e')):
        print(f"{chr(juan)}", end="")

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_list = [1, 2, 3, 4,5,]
    try:
        for elm in my_list:
            print(elm, end="")
            x = x + 1
        print(x, end="")
    except ValueError:
        pass
safe_print_list()

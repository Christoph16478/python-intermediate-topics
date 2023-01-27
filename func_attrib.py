#!/usr/bin/python3
# -*- coding: utf-8 -*-

def my_func(x_value: list):
    """add 1 every iteration in the range
    """
    val_f = 1
    for i in x_value:
        val_f += 1
    return val_f

def print_function_output(func, **kwargs):
    """print out arguments
    """
    print(func(**kwargs))

def grow_list(val, my_list=None):
    """grow a list of values
    """
    if my_list:
        my_list.append(val)
    else:
        my_list = [val]
    return my_list

def main():
    """main program
    """
    # print_function_output(my_func, val=10)
    my_func([1,2,3,4])
    print(dir(grow_list))
    print(grow_list.__defaults__)
    print(grow_list.__name__)
    print(grow_list.__code__.co_argcount)
    print(grow_list.__code__.co_varnames)

if __name__ == "__main__":
    main()

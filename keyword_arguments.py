#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
normal args; *ARGS;
default args; **KWARGS
*ARGS: tuple
**KWARGS: dict
"""

import matplotlib.pyplot as plt

def plot_my_lists(list_x, list_y, **kwargs):
    """plot list
    """
    print(plt.scatter(list_x, list_y, **kwargs))
    print(plt.show())

def my_function_1(a, *args, x=2, y=3, z=4, **kwargs):
    """get values of args and kwargs plus type
    plus normal arguments
    """
    print(args, type(args))
    print(kwargs, type(kwargs))
    print(f'a: {a}, x: {x}, y: {y} , z: {z}, args: {args}, kwargs: {kwargs}')

def my_function_2(*args, **kwargs):
    """get values of args and kwargs plus type
    """
    print(args, type(args))
    print(kwargs, type(kwargs))
    print(f'args: {args}, kwargs: {kwargs}')

def my_function_3(a, *args, **kwargs):
    """get values of args and kwargs plus type
    """
    print(a)
    a *= 2
    print(a)
    print(args, type(args))
    print(kwargs, type(kwargs))
    print(f'args: {args}, kwargs: {kwargs}')

def main():
    """main program
    """
    my_function_1(1, 3, 4, x=13.37, b=False, c=30, d=40.5)
    my_function_2(1, 3, 4, x=13.37, b=False, c=30, d=40.5)
    my_function_3(1, 3, 4, x=13.37, b=False, c=30, d=40.5)

    list_x = [-3, -2, -1, 1, 2, 3]
    list_y = [9, 4, 1, 1, 4, 9]
    plot_my_lists(list_x, list_y, c='red')

if __name__ == "__main__":
    main()






































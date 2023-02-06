#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""module demonstrates function attributes
"""

def grow_list(val=None, my_list=None):
    """append a list with values
    """
    if my_list:
        my_list.append(val)
    else:
        my_list = [val]
    return my_list

def main():
    """main program
    """
    print(dir(grow_list)) # return all function attributes
    print(grow_list.__name__) # return function name
    print(grow_list.__doc__) # return function docstring
    print(grow_list.__defaults__) # return all default values of function parameters    
    print(grow_list.__code__.co_argcount) # return number of arguments
    print(grow_list.__code__.co_varnames) # return all paramter names

if __name__ == "__main__":
    main()

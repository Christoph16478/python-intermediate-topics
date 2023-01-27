#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import wraps

# Decorators:
# - wraps a function by another function
# - takes a function as an argument, returns a closure
# - the clousure runs the previous passed in function with the *args and **kwargs arguments

def outer_fn(fn):
    """outer function
    """
    def inner_fn():
        fn_result = fn()
        return fn_result
    return inner_fn

def print_hello_world():
    """print Hello World
    """
    print("Hello World!")

decorated_print_hello_world = outer_fn(print_hello_world)
decorated_print_hello_world()

def decorator(fn):
    """decorator
    """
    print("Start decorator function from: ", fn.__name__)
    def wrapper(*args, **kwargs):
        print("Start wrapper function from: ", fn.__name__)
        fn_result = fn(*args, **kwargs)
        print("End wrapper function from: ", fn.__name__)
        return fn_result
    print("End decorator function from: ", fn.__name__)
    return wrapper

def print_arguments(a, b, c=None):
    """print arguments
    """
    print(f"a: {a}, b: {b}, c: {c}")

decorated_print_arguments = decorator(print_arguments)
decorated_print_arguments(a=10, b=20, c=30)
decorated_print_arguments(a=11, b=21, c=31)

@decorator
def print_arguments2(a, b, c=None):
    """print arguments
    """
    print(f"a: {a}, b: {b}, c: {c}")

print_arguments2(a=10, b=20, c=30)

# decorator example

def debug(fn):
    """debug function
    """
    @wraps(fn)
    def debugger(*args, **kwargs):
        args_values_types = [(a, type(a)) for a in args]
        kwargs_values_types = [(k, v, type(v)) for k, v in kwargs.items()]
        print(f"Args: {args_values_types}")
        print(f"Kwargs: {kwargs_values_types}")
        print(f"Function {fn.__name__} called")
        fn_result = fn(*args, **kwargs)
        print(f"Function {fn.__name__} returns: {fn_result}")
        return fn_result
    return debugger

@debug
def do_something(a, b, c=None):
    """Do something.
    """
    return a + b if c else 0

@debug
def do_something2(a, b, c=None):
    """do_something2
    """
    return a - b if c else 0

@debug
def do_something3(a, b, c=None):
    """do_something3
    """
    return a * b if c else 0

@debug
def do_something4(a, b, c=None):
    """do_something4
    """
    return a / b if c else 0

def main():
    """main program
    """
    decorated_print_hello_world2 = decorator(print_hello_world)
    decorated_print_hello_world2()

    do_something(10, 20, c=1)
    do_something2(10, 20, c=1)
    do_something3(10, 20, c=1)
    do_something4(10, 20, c=1)

if __name__ == "__main__":
    main()

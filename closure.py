#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""demonstration of closures: nested function that
allows access variables of the outer function even
after the outer function is already closed
"""

import time

def outer_fn(message):
    """outer function for closure example
    """
    outer_message = "Outer: " + message
    print(outer_message)
    current_time = time.time()
    print(current_time)

    def inner_fn():
        """inner function: a closure is an inner function that has
        access to variables in the local scope of the outer function
        """
        print("Inner: '" + outer_message + "'")
        print("Current time: ", current_time)
    return inner_fn()

def main():
    """main program
    """
    outer_fn("Hello World!")

if __name__ == "__main__":
    main()

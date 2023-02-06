#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""demonstration of closures: nested function that
allows access variables of the outer function even
after the outer function is already closed
"""

import time

def outer_function(msg) -> None:
    """outer function for closure example
    """
    outer_msg = "Outer: " + msg
    print(outer_msg)
    current_time = time.time()
    print(current_time)

    def inner_function() -> None:
        """inner function: a closure is an inner function that has
        access to variables in the local scope of the outer function
        """
        print("Inner: '" + outer_msg + "'")
        print("Current time: ", current_time)
    return inner_function()

def main() -> None:
    """main program
    """
    outer_function("Hello World!")

if __name__ == "__main__":
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""decorators wraps a function by anotherone. It takes
a function as an argument and returns a closure. The
closure runs the previous in function with the *args
and **kwargs arguments.
"""

from functools import wraps

def debug(param_func) -> None:
    """debug function
    """
    @wraps(param_func)
    def debugger(*args, **kwargs) -> None:
        """debugger
        """
        args_values_types = [(a, type(a)) for a in args]
        kwargs_values_types = [(k, v, type(v)) for k, v in kwargs.items()]
        print(f"Args: {args_values_types}")
        print(f"Kwargs: {kwargs_values_types}")
        fn_result = param_func(*args, **kwargs)
        print(f"Function {param_func.__name__} returns: {fn_result}")
        return fn_result
    return debugger

@debug
def calculate_sum(val_a: int, val_b: int, res_c: int=None) -> int:
    """calculate the sum
    """
    return val_a + val_b if res_c else 0

def main() -> None:
    """main program
    """
    calculate_sum(2,2,4)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""special parameters
"""

import time
from classes.Calculations import Calculations

calc: Calculations = Calculations()

def main():
    """main program
    """
    start_time = time.perf_counter()

    for _ in range(4):
        calc.calc_square(10)

    end_time = time.perf_counter()
    print(f"Took: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()

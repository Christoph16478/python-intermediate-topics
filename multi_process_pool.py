#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Test code.
"""

import time
import itertools
from multiprocessing import Pool
from classes.Calculations import Calculations

NUM_PROCESSES = 4

def main():
    """main program
    """
    start_time = time.perf_counter()
    clc2: Calculations = Calculations()
    with Pool(processes=NUM_PROCESSES) as pool:
        pool.map(clc2.calc_square(100), itertools.repeat(8_000_000, NUM_PROCESSES))

    end_time = time.perf_counter()
    print(f"Took: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()

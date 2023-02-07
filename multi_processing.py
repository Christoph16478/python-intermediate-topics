#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""multi processing demonstration
"""

import time
from multiprocessing import Process
from classes.Calculations import Calculations

NUM_PROCESSES = 4

def main():
    """main program
    """
    processes = []

    clc1: Calculations = Calculations()

    for _ in range(NUM_PROCESSES):
        processes.append(Process(target=clc1.calc_square, args=[2]))

    start_time = time.perf_counter()

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.perf_counter()
    print(f"Took: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()

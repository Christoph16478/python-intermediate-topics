#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""multi threading demonstration
"""

import time
from threading import Thread
from classes.Calculations import Calculations

NUM_THREADS = 4

def main():
    """main program
    """
    threads = []
    clc: Calculations = Calculations()
    for _ in range(NUM_THREADS):
        threads.append(Thread(target=clc.calc_square(100), args=[8_000_000]))

    start_time = time.perf_counter()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    print(f"Took: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()

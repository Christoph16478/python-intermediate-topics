#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""profiling demonstration
"""

import cProfile
import pstats
import io
import random
from functools import wraps

from classes.Vector2D import Vector2D

def profile(f_n):
    """profile
    """
    @wraps(f_n)
    def profiler(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        f_n_result = f_n(*args, **kwargs)
        profiler.disable()
        stream = io.StringIO()
        ps = pstats.Stats(profiler, stream=stream).sort_stats('time')
        ps.print_stats()
        print(stream.getvalue())
        return f_n_result
    return profiler

@profile
def test_addition():
    """test addition
    """
    for _ in range(100_000):
        vector_1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        vector_2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        sum_3 = vector_1 + vector_2
        return sum_3

def main():
    """main program
    """
    test_addition()

if __name__ == "__main__":
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

class Calculations:
    """class represents all sorts of calculations
    """

    def __init__(self) -> None:
        """initialize class
        """

    def calc_square(self, num_elements: int) -> int:
        """take each number of elements and calulate the
        power of the total number them
        """
        res = 0
        for i in range(num_elements):
            res += math.sqrt(i)
        print(res)
        return res

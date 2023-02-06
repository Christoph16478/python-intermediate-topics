#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""print out memory addresses of variable values
"""

import random
from classes.Memory import Memory

def append_random_value(full_list: list) -> None:
    """append a random value
    """
    full_list.append(random.randint(-100, 100))

def main() -> None:
    """main program"""
    mem_1: Memory = Memory()
 
    my_int_val_1: int = 100
    my_int_val_2: int = 100
    print(mem_1.get_mem_addr(my_int_val_1))
    # 0x1c0b01b0d50
    print(mem_1.get_mem_addr(my_int_val_2))
    # 0x1c0b01b0d50

    my_int_val_1: int = 1000
    my_int_val_2: int = 1000
    print(mem_1.get_mem_addr(my_int_val_1))
    # 0x1c0b2bb5e30
    print(mem_1.get_mem_addr(my_int_val_2))
    # 0x1c0b2bb5e30

    my_list1 = []
    print(random.seed(42))
    # None
    append_random_value(my_list1)
    print(my_list1)
    # [63]

if __name__ == "__main__":
    main()














































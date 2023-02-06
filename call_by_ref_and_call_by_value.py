#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""demonstrates call by value and call by
reference
"""

value_1: str = "random string"

def test_function(value_1: str) -> str:
    """call by value
    """
    value_1 = "another random test string"
    print(f"Inside {test_function.__name__} function: {value_1}")

    return value_1

def add_more(my_list: list) -> list:
    """call by reference
    """
    list.append(50)
    print(f"Inside {add_more.__name__} function: {my_list}")

    return list

def main() -> None:
    """main program
    """
    # call by value
    test_function(value_1)
    print(f"Outside {test_function.__name__} function: {value_1}")
    # call by reference
    list_1 = [10,20,30,40]
    add_more(list_1)
    print(f"Outside {add_more.__name__} function: {list_1}")

if __name__ == "__main__":
    main()

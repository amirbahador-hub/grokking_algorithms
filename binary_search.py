import sys
import math


def binary_search(list_, item):
    low = 0
    high = len(list_) - 1    # high index pointer
    while low <= high:       # if element not in the list then => low > high
        mid = (low + high) // 2
        guess = list_[mid]
        if guess == item:
            return mid       # element index  found
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None  # if element is not in the list


def calculate_bs_worst_case(list_num):
    max_steps = math.log2(list_num)
    print(f"worst case scenario maximum {math.ceil(max_steps)} steps is required")


def main(element):
    my_list = [1, 3, 7, 5, 9]
    calculate_bs_worst_case(len(my_list))
    answer = binary_search(my_list, element)
    print(answer)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(8)


# python binary_search.py 7

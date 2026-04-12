#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    # Initialize total swaps counter
    total_swaps = 0

    # Bubble Sort Algorithm
    for i in range(n):
        # Track swaps for this specific pass
        number_of_swaps = 0
        
        for j in range(n - 1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                number_of_swaps += 1
                total_swaps += 1
        
        # If no elements were swapped during a traversal, array is sorted
        if number_of_swaps == 0:
            break

    # Print required output
    print(f"Array is sorted in {total_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

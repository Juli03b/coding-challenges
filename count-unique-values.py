from typing import List


def countUniqueValues(lst: List) -> int:
    """
    Implement a function, countUniqueValues, which accepts a sorted array, and counts unique values in array.
    There can be negative numbers in the array, but it will always be sorted.

    Pseudocode:
        count = 0
        i = 0
        j = 1
        while i < length(lst):
            if lst[i] is not lst[j] and j < len(lst):
                j += 1
            elif lst[i] == lst[j]:
                count += 1
                i += 1
                j = 0
            elif j >= len(lst):
                i += 1
                j = 0
    """
    count = 0
    i = 0
    j = len(lst) - 1
    while i < len(lst):
        if lst[i] is not lst[j] and j < len(lst):
            j -= 1
        elif lst[i] == lst[j]:
            count += 1
            i += 1
            j = 0
        elif j >= len(lst):
            i += 1
            j = 0
    return count

print(countUniqueValues([1, 1, 1, 1, 1, 2])) # 2
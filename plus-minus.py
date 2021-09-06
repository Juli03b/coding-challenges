# LINK TO HACKERRANK: https://www.hackerrank.com/challenges/plus-minus/problem
from typing import List

def plusMinus(array: List[int]) -> None:
    """
    Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
    Print the decimal value of each fraction on a new line with  places after the decimal.

    Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
     though answers with absolute error of up to  are acceptable.

    Example:

        There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

        0.400000
        0.400000
        0.200000

    Function Description:

        plusMinus has the following parameter(s):

            int arr[n]: an array of integers
            Print the ratios of positive, negative and zero values in the array. 
            Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

        Input Format:

            The first line contains an integer, , the size of the array.
            The second line contains  space-separated integers that describe .
    """
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # Use a set to get all numbers once and loop through them
    for num in set(array):
        count = array.count(num)
        if num > 0:
            positive_count += count
        elif num < 0:
            negative_count += count
        elif num == 0:
            zero_count += count

    positive_ratio = format(positive_count / len(array), '.6f')
    negative_ratio = format(negative_count / len(array), '.6f')
    zero_ratio = format(zero_count / len(array), '.6f')

    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)

print(plusMinus([-4, 3, -9, 0, 4, 1]))
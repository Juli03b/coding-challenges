# LINK TO LEETCODE: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a
    specific target number. Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
    where 1 <= answer[0] < answer[1] <= numbers.length.

    Example 1:

        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

    Example 2:

        Input: numbers = [2,3,4], target = 6
        Output: [1,3]

    Example 3:

        Input: numbers = [-1,0], target = -1
        Output: [1,2]
    """
    i = 0
    j = len(numbers) - 1
    
    while i < j:
        i_val = numbers[i]
        j_val = numbers[j]
        ij_sum = i_val + j_val

        if ij_sum == target:
            return [i + 1, j + 1]
        if ij_sum > target: # if the sum of vals at i and j is greater than target, it means that val at j is too large
            j -= 1
        else:   # Else, val at i is too small
            i += 1

# [5, 10, 12, 23, 25, 32, 75]
# print(twoSum([5, 10, 12, 23, 25, 32, 75], 30))

# [5,25,75]
# 100
# print(twoSum([5,25,75], 100))

# [2,7,11,15]
# 9
# print(twoSum([2,7,11,15], 9))
# [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
# 542
print(twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997], 542))
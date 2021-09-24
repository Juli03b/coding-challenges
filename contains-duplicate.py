# LINK TO LEETCODE: https://leetcode.com/problems/contains-duplicate/

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element
     is distinct.

    Example 1:

        Input: nums = [1,2,3,1]
        Output: true
    
    Example 2:

        Input: nums = [1,2,3,4]
        Output: false
    
    Example 3:

        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true
    """
    if not nums: return False
    int_frequency = dict()
    for num in nums:
        int_frequency[num] = int_frequency.get(num, 0) + 1
        if int_frequency[num] > 1:
            return True
    return False
    
print(containsDuplicate([1,2,3,4]))
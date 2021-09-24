# Link to LeetCode: https://leetcode.com/problems/maximum-product-subarray/

from typing import List

def maxProduct(nums: List[int]) -> int:
    """
    Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the
    product. It is guaranteed that the answer will fit in a 32-bit integer. A subarray is a contiguous subsequence of the array.

    Example 1:

        Input: nums = [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.

    Example 2:

        Input: nums = [-2,0,-1]
        Output: 0
        Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    """
    if not nums: return 0
    if len(nums) == 1: return nums[0]

    largest_product = 0
    
    for i, num in enumerate(nums):
        print(num)
        product = num * (((len(nums) > i + 1) and nums[i + 1]) or 1)
        
        # Multiply the current value by the next value or 1 if next is null
        if product > largest_product:
            print("PRODUCTL", product)
            largest_product = product

    return largest_product

# print(maxProduct([-4,-3]))
# print(maxProduct([-2,0]))
# print(maxProduct([0]))
print(maxProduct([-2,3,-4]))
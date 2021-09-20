# LINK TO LEETCODE: https://leetcode.com/problems/3sum/
from typing import List
# INCOMPLETE!
def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
    and nums[i] + nums[j] + nums[k] == 0.

    Pseudocode:
        results = []
        i_dict = dictionary instantiation to store indicies by their values
        Loop i, num in nums:
            Loop j, numJ in nums + 1:
                summed = num + numJ + num[j + 1]
                if summed == 0:
                    results.push([i, j, j + 1])
        Return results
    
    Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]

    Example 2:
        Input: nums = []
        Output: []

    Example 3:
        Input: nums = [0]
        Output: []
    """
    if not nums: return []
    results = []
    for i, num in enumerate(nums):
        for j, numJ in enumerate(nums[i + 1: -1], i + 1):
            triplets = [num, numJ, nums[j + 1]]
            duplicate = False
            for res in results:
                mins = set(res) - set(triplets)
                if not mins:
                    duplicate = True
                    break
            if duplicate: break
            summed = sum(triplets)
            if summed == 0:
                results.append(triplets)
    return results

print(threeSum([-1,0,1,2,-1,-4]))
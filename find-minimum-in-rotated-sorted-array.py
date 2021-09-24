from typing import List
from math import floor
# Unfinished
def findMin(nums: List[int]) -> int:
    """sort then check the differences of indicies in the first array"""
    i = 0
    j = len(nums) - 1

    while i < j:
        mid_point_idx = floor((i + j) / 2)
        mid_point_value = nums[mid_point_idx]
        print("MID POINT", mid_point_value)
        left_point_value = nums[i]
        right_point_value = nums[j] 
        print("left poiun", left_point_value)
        print("right poiun", right_point_value)

        if left_point_value >= mid_point_value and right_point_value >= mid_point_value:
            return mid_point_value
            
        # If left value is greater than current value go right
        if nums[mid_point_idx - 1] > mid_point_value and right_point_value > mid_point_value:
            i = mid_point_idx + 1
            
        # If right value is greater than current value go left
        elif nums[mid_point_idx + 1] > mid_point_value and left_point_value < mid_point_idx:
            j = mid_point_idx - 1
        
        # If left value is less than current value got left
        elif nums[mid_point_idx - 1] < mid_point_value and right_point_value > mid_point_value: 
            j = mid_point_idx - 1

        # If right value is less than current value go right
        elif nums[mid_point_idx + 1] < mid_point_value and left_point_value < mid_point_idx: 
            i = mid_point_idx + 1
        elif left_point_value < right_point_value:
            j = mid_point_idx - 1
        else:
            i = mid_point_idx + 1
 
    return nums[0]
    # return first_num_idx_sorted + 1

# print(findMin([3,4,5,1,2]))
# print(findMin([11,13,15,17]))
print(findMin([4,5,6,7,0,1,2]))
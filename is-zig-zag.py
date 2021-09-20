from typing import List
def zig_zag_checker(a: int, b:int, c: int):
    if a == b and b == c:
        return 0
    if a < b > c or a > b < c:
        return 1
    return 0
def is_zig_zag(nums: List[int]):
    """
    Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c. Given an array of integers numbers, your task is 
    to check all the triples of its consecutive elements for being a zigzag. More formally, your task is to construct an array
    of length numbers.length - 2, where the ith element of the output array equals 1 if the triple (numbers[i], numbers[i + 1],
    numbers[i + 2]) is a zigzag, and 0 otherwise.

    Ideas:
        1. 
            - Create an array to hold 0 or 1's to represent if a triple was a zigzag. 
                The length of this array will be nums.length - 2
                Array name: zig_zags
            - Create another function that accepts three intigers: a, b, and c. 
                It checks if the inputs are all the same. 
                If they are, return 0. Then, it checks if a < b > c or a > b < c, and if either statement is true, then return 1.
                Function name: zig_zag_checker
            - Loop over nums from indicies of 0 to it's length - 2.
                zig_zag_int = Get 1 or 0 from zig_zag_checker(i, i + 1, i + 2)
                zig_zags.append(zig_zag_val)

    Example 1:

        For numbers = [1, 2, 1, 3, 4], the output should be isZigzag(numbers) = [1, 1, 0].

        (numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;
        (numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;
        (numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;

    Example 2:
    
        For numbers = [1, 2, 3, 4], the output should be isZigzag(numbers) = [0, 0];
        Since all the elements of numbers are increasing, there are no zigzags.

    Example 2:
    
        For numbers = [1000000000, 1000000000, 1000000000], the output should be isZigzag(numbers) = [0].
        Since all the elements of numbers are the same, there are no zigzags.

    Guaranteed constraints:
        3 ≤ numbers.length ≤ 100,
        1 ≤ numbers[i] ≤ 109.
    """
    if not nums: return 0
    zig_zags = [] # Initialize zig zag array
    nums_split = nums[:-2]

    for i, num in enumerate(nums_split):
        zig_zag_int = zig_zag_checker(num, nums[i + 1], nums[i + 2])
        zig_zags.append(zig_zag_int)
    return zig_zags

# print("RES:", is_zig_zag([1, 2, 1, 3, 4]) ,"\nSHOULD BE:", "[1, 1, 0]")
print("RES:", is_zig_zag([1000000000, 1000000000, 1000000000]) ,"\nSHOULD BE:", "[0]")
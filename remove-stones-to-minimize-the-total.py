# LINK TO LEET CODE: https://leetcode.com/problems/remove-stones-to-minimize-the-total/
from typing import List
from math import floor
# Incomplete -> need to determine how to choose i
def minStoneSum(piles: List[int], k: int) -> int:
    """
    You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k.
    You should apply the following operation exactly k times:

        Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
        Notice that you can apply the operation on the same pile more than once.

        Return the minimum possible total number of stones remaining after applying the k operations.

        floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).

    Example 1:

        Input: piles = [5,4,9], k = 2
        Output: 12
        Explanation: Steps of a possible scenario are:
        - Apply the operation on pile 2. The resulting piles are [5,4,5].
        - Apply the operation on pile 0. The resulting piles are [3,4,5].
        The total number of stones in [3,4,5] is 12.

    Example 2:

        Input: piles = [4,3,6,7], k = 3
        Output: 12
        Explanation: Steps of a possible scenario are:
        - Apply the operation on pile 2. The resulting piles are [4,3,3,7].
        - Apply the operation on pile 3. The resulting piles are [4,3,3,4].
        - Apply the operation on pile 0. The resulting piles are [2,3,3,4].

    The total number of stones in [2,3,3,4] is 12.
    """
    # loop through all piles
    for i in range(k):
        print("i",i)
        j = (len(piles) - i) + 1
        if j >= len(piles):
            j = 0
        print("J", j)
        pile = piles[j]
        piles[i] = pile - floor(pile / 2)
        print(piles)
    return sum(piles)
    # total_stones = 0
    # for i in range(k, -1, -1):
    #     print("I",i)
    #     pile = piles[i]
    #     stones_to_remove = floor(pile / 2)
    #     total_stones += pile - stones_to_remove

    # return total_stones
print(minStoneSum([4,3,6,7], 3))
# print(minStoneSum([5,4,9], 2))
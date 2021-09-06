# LINK TO HACKER RANK: https://hr.gs/eabbdd 
from typing import List

def sock_merchant(a_len: int, array: List[int]):
    """
    There is a large pile of socks that must be paired by color. Given an array of integers representing
     the color of each sock, determine how many pairs of socks with matching colors there are.

    Example:
    
        There is one pair of color and one of color .There are three odd socks left, one of each color. The number of pairs is .
    
    Function Description:
    
        Complete the sockMerchant function in the editor below.
        sockMerchant has the following parameter(s):
        int n: the number of socks in the pile
        int ar[n]: the colors of each sock
        Returns
        int: the number of pairs
    
    The first line contains an integer , the number of socks represented in .
    The second line contains  space-separated integers, , the colors of the socks in the pile.
    
    >>> sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
    3
    """
    # sort socks for quicker traversing, avoid O(n^2)
    array.sort()

    pairs = 0
    i = 0

    while i < a_len - 1:
    # loop through every number in the array
        current_num = array[i]
        next_num = array[i + 1]
        # check if the current number pairs with the next one
        if current_num == next_num:
            pairs += 1
            i += 1
        i += 1
        

    return pairs

print(sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
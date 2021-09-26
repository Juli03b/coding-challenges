# Link to LeetCode: https://leetcode.com/problems/n-th-tribonacci-number/

def tribonacci(n: int) -> int:
    """
    The Tribonacci sequence Tn is defined as follows: 

        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

    Given n, return the value of Tn.
    
    Example 1:

        Input: n = 4
        Output: 4
        Explanation:
        T_3 = 0 + 1 + 1 = 2
        T_4 = 1 + 1 + 2 = 4

    Example 2:

        Input: n = 25
        Output: 1389537
    """
    if n == 0: return 0

    fib_nums = [0] * (n * 3)
    
    fib_nums[0] = 0
    fib_nums[1] = 1
    fib_nums[2] = 1

    for i in range(0, n):
        fib_nums[i + 3] = fib_nums[i] + fib_nums[i + 1] + fib_nums[i + 2]
    
    return fib_nums[n]

print(tribonacci(1))
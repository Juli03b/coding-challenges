# Link to LeetCode: https://leetcode.com/problems/fibonacci-number/

def fib(n: int):
    """
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum
     of the two preceding ones, starting from 0 and 1. That is,

    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).

    Idea: Bottom up
        if n is false return 0
        if n is 1 return 1

        Setup array storing numbers of n length
        Set first two values of arrray to 1
        
        Loop i from 2 to n:
            sum = n[i - 1] + n[i - 2] # Add two values before current one
            array[i] = sum  # Set i of numbers array to the sum
        
        return array[n]

    Example 1:

        Input: n = 2
        Output: 1
        Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

    Example 2:

        Input: n = 3
        Output: 2
        Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

    Example 3:

        Input: n = 4
        Output: 3
        Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
    """
    if n == False: return 0
    if n == 1: return 1

    fib_nums = [0] * n
    fib_nums[0] = 1
    fib_nums[1] = 1

    for i in range(2, n):
        print("I", i)
        print("IFIB",fib_nums)
        fib_sum = fib_nums[i - 1] + fib_nums[i - 2] # Add two values before current one
        fib_nums[i] = fib_sum  # Set i of numbers array to the sum
    
    return fib_nums[n - 1]
print(fib(8))
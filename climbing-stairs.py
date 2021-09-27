# Link to LeetCode https://leetcode.com/problems/climbing-stairs/
def climb_stairs(n: int):
    """
    You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.
     In how many distinct ways can you climb to the top?

    Idea:
        Like fib, except base nums are 1 and 2

    Example 1:

        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

    Example 2:

        Input: n = 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
    """
    if n == 0: return 0
    if n == 1: return 1

    step_one = 1
    step_two = 2
    total = 0
    for _ in range(2, n):
        step_two_temp = step_two
        step_one = step_two + 1
        step_two = step_two_temp + 1
        total = step_one + step_two
        
    return total

print(climb_stairs(45), "should be:", "1836311903")

# Solution 2
"""    if n == 0: return 0
    if n == 1: return 1

    steps = [0] * n
    steps[0] = 1
    steps[1] = 2
    
    for i in range(2, n):
        steps[i] = steps[i - 1] + steps[i - 2]


    return steps[n - 1]
"""
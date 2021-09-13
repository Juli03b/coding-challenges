def staircase(n: int):
    """
    This is a staircase of size :

    n = 4
    
    #
    ##
    ###
    ####

    Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
    Write a program that prints a staircase of size.

    staircase has the following parameter(s):
        int n: an integer
        A single integer, denoting the size of the staircase.

    Note: The last line must have spaces in it.

    Sample Input: 6 
    Sample Output

    #
    ##
    ###
    ####
    #####
    ######

    Explanation:

        The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .
    """
    spaces = 0
    for i in range(n + 1):
        print(" " * spaces, "#" * i)

print(staircase(4))
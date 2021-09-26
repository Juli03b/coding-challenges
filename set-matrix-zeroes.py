from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
    You must do it in place.

    Example 1:

        Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
        Output: [[1,0,1],[0,0,0],[1,0,1]]
        
    Example 2:

        Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    """
    column_index_with_zeroes = set()
    for i, arr in enumerate(matrix):
        for j, n in enumerate(arr):
            if n == 0:
                # Set values in row to just zeroes
                matrix[i] = [0] * len(arr)
                # Save column index that has a zero
                column_index_with_zeroes.add(j)
                
    # With column indicies, set values to zero
    for i, _ in enumerate(matrix):
       for j in column_index_with_zeroes:
           matrix[i][j] = 0
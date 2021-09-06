# LINK TO LEETCODE: https://leetcode.com/problems/path-sum/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], target_sum: int) -> bool:
    """
    Given the root of a binary tree and an integer targetSum, return true if the tree has a 
     root-to-leaf path such that adding up all the values along the path equals targetSum.
    A leaf is a node with no children.

    Picture: https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg

    Example 1:

        Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
        Output: true

    Example 2:

        Input: root = [1,2,3], targetSum = 5
        Output: false

    Example 3:

        Input: root = [1,2], targetSum = 0
        Output: false
    """

    if not root: return False

    left_node = root.left
    right_node = root.right
    # check if at a leaf node and if at target sum
    if not left_node and not right_node and target_sum - root.val == 0: return True
    # Else, append left and/or right nodes to stack
    return hasPathSum(left_node, target_sum - root.val) or hasPathSum(right_node, target_sum - root.val)


print(hasPathSum(TreeNode(1, right=TreeNode(3)), 5))

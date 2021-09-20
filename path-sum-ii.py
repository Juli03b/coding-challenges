# Definition for a binary tree node.
from typing import List, Optional
from operator import attrgetter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"<TreeNode val={self.val} left={self.left} right={self.right}>"

def path_sum(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in
    the path equals targetSum. Each path should be returned as a list of the node values, not node references. A root-to-leaf path
    is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

    Ideas:
        1 - Use DFS to go to leaf nodes. While traversing the tree, keep an array to hold values of the current root to leaf.
        It resets when were at the leaf node and the current_sum doesn't equal the target_sum. I think that the nodes should 
        be added to the stack with the current_sum, in a tuple.

    Example 1:

        Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
        Output: [[5,4,11,2],[5,8,4,5]]
        Explanation: There are two paths whose sum equals targetSum:
        5 + 4 + 11 + 2 = 22
        5 + 8 + 4 + 5 = 22

    Example 2:

        Input: root = [1,2,3], targetSum = 5
        Output: []

    Example 3:

        Input: root = [1,2], targetSum = 0
        Output: []
        
    Constraints:

        The number of nodes in the tree is in the range [0, 5000].
        -1000 <= Node.val <= 1000
        -1000 <= targetSum <= 1000
    """
    if not root: return []

    valid_sum_paths = []
    node_stack = [(root, root.val, [root.val])]

    while node_stack:
        current_node, current_sum, current_path_vals = node_stack.pop()
        left, right = attrgetter("left", "right")(current_node)

        if not left and not right:
            if current_sum == target_sum:
                valid_sum_paths.append(current_path_vals)
        if left:
            node_stack.append((left, left.val + current_sum, [*current_path_vals, left.val]))
        if right:
            node_stack.append((right, right.val + current_sum, [*current_path_vals, right.val]))

    return valid_sum_paths

print(path_sum(TreeNode(23, TreeNode(12), TreeNode(53)), 76))
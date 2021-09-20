# LINK TO LEETCODE: https://leetcode.com/problems/binary-tree-paths/
from typing import List, Optional
from operator import attrgetter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"<TreeNode val={self.val} left={self.left} right={self.right}>"

def make_path_string(current_path_string: str, to_add: int):
    return current_path_string + (f"->{to_add}" if current_path_string[-1].isdigit() else f"{to_add}")

def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    """
    Given the root of a binary tree, return all root-to-leaf paths in any order. A leaf is a node with no children.
    
    Pseudocode:
        Do a DFS with a stack. Nodes should be appended in a tuple with the current_node and the nodes string.

    Example 1:

        Input: root = [1,2,3,null,5]
        Output: ["1->2->5","1->3"]

    Example 2:

        Input: root = [1]
        Output: ["1"]
    """
    if not root: return []
    root_to_leaf_path_strings = []
    node_stack = [(root, f"{root.val}")]

    while node_stack:
        current_node, current_path_string = node_stack.pop()
        left, right = attrgetter("left", "right")(current_node)

        if not left and not right:
            root_to_leaf_path_strings.append(current_path_string)
        if left:
            left_path_string = make_path_string(current_path_string, left.val)
            node_stack.append((left, left_path_string))
        if right:
            right_path_string = make_path_string(current_path_string, right.val)
            node_stack.append((right, right_path_string))
    return root_to_leaf_path_strings

def to_binary_tree(items: List[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion to build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()
btn = to_binary_tree([1])

print(binary_tree_paths(btn))
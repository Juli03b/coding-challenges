from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    """
    Given the head of a singly linked list, return true if it is a palindrome.

    Pseudocode:
        node_vals = array
        current_node = head
        while current_node:
            node_vals.push(current_node.val)
        if reversed(node_vals) == node_vals:
            return true
        Return false

    Example 1:

        Input: head = [1,2,2,1]
        Output: true

    Example 2:

        Input: head = [1,2]
        Output: false
    """
    node_vals = []
    current_node = head
    
    while current_node:
        node_vals.append(current_node.val)
        current_node = current_node.next
    if node_vals[-1::-1] == node_vals:
        return True
    return False
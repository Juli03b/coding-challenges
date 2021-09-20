# LINK TO LEETCODE: https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return (f"<ListNode val={self.val} next={self.next}>")

def reverseListNoob(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Pseudocode:
        reversed_list_head = ListNode
        reversed_list = reversed_list_head
        list_values = []
        current_node = head

        while head:
            linked_list_values.append(current_node.val)
            current_node = current_node.next
        
        for val in reversed(list_values):
            reversed_list.val = val
            reversed_list.next = ListNode
            reversed_list = reversed_list.next

    Example 1:

        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]

    Example 2:

        Input: head = [1,2]
        Output: [2,1]

    Example 3:

        Input: head = []
        Output: []
    
    """
    reversed_list_head = ListNode()
    reversed_list = reversed_list_head
    list_values = []
    current_node = head

    while current_node:
        list_values.append(current_node.val)
        current_node = current_node.next

    for val in list_values[-1::-1]:
        reversed_list.val = val
        next_node = ListNode()
        reversed_list.next = next_node
        reversed_list = next_node
    
    return reversed_list_head

def reverseListIterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Traverse list, store next and previous nodes to set the current node's next property to the previous node,
    and the next node's next is the current node.
    Pseudocode:
        current_node = head
        next_node = null
        prev_node = null
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return head

    Example 1:

        Input: head = [1,2,3,4,5] 
        Looping through list. At 3, next the next_node to 4. Set current_node.next to 
        Output: [5,4,3,2,1]

    """
    next_node = None
    prev_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node

# [1,2,3,4,5]

print(reverseListIterative(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
# print(reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
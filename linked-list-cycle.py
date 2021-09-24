# Link to LeetCode: https://leetcode.com/problems/linked-list-cycle/
from data_structures.singly_linked_list import ListNode

def hasCycle(head: ListNode) -> bool:
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if
    there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used
    to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter. Return
    true if there is a cycle in the linked list. Otherwise, return false.

    Example 1:

        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

    Example 2:

        Input: head = [1,2], pos = 0
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
    """
    seen_nodes = set()
    current_node = head
    while current_node:
        have_seen = current_node in seen_nodes
        if have_seen:
            return True

        seen_nodes.add(current_node)
        current_node = current_node.next

    return False
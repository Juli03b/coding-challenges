# Link to LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from data_structures.singly_linked_list import ListNode
from helper_functions.list_to_singly_linked_list import list_to_linked_list
from typing import Optional

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Example 1:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]

    Example 2:
        Input: head = [1], n = 1
        Output: []

    Example 3:
        Input: head = [1,2], n = 1
        Output: [1]
    """
    current_node = head
    get_nodes_by_index = dict()
    idx = 0

    # Loop through nodes
    while current_node:
        # Store nodes in dict by index
        idx += 1
        get_nodes_by_index[idx] = current_node
        current_node = current_node.next

    # Get previous node and next node from the index of the node to be removed
    previous_node = get_nodes_by_index.get((idx - n))
    next_node = get_nodes_by_index.get((idx - n) + 2)
    
    if not previous_node:
        return next_node

    previous_node.next = next_node

    return head

# print(removeNthFromEnd(list_to_linked_list([1,2,3,4,5]), 2))
print(removeNthFromEnd(list_to_linked_list([1,2]), 1))
# print(removeNthFromEnd(list_to_linked_list([1]), 1))


# Solution 2
# for i in range(idx - n):
#     previous_node = current_node
#     current_node = current_node.next
# previous_node.next = current_node.next
# return head
# length = 0
# current_node = head
# while current_node:
#     length += 1
#     # nodes_dict[idx] = {"current_node": current_node,"last_node": last_node}
#     # last_node = current_node
#     current_node = current_node.next
# # print(nodes_dict)
# current_node = head
# previous_node = None
# for i in range(length - n):
#     previous_node = current_node
#     current_node = current_node.next
# previous_node.next = current_node.next
# return head

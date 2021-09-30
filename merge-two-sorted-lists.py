from typing import Optional
from data_structures.singly_linked_list import ListNode
from helper_functions.list_to_singly_linked_list import list_to_singly_linked_list

def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the
    first two lists.
    
    Example 1:

        Input: l1 = [1,2,4], l2 = [1,3,4]
        Output: [1,1,2,3,4,4]

    Example 2:

        Input: l1 = [], l2 = []
        Output: []

    Example 3:

        Input: l1 = [], l2 = [0]
        Output: [0]
    """
    if not l1 and not l2: return l1
    if not l1 and l2: return l2
    if not l2 and l1: return l1
    if not l1.next:
        current_l2_node = l2

        # Go to end of list
        while current_l2_node.next:
            if current_l2_node.next.val > l1.val:
                break
            current_l2_node = current_l2_node.next
        
        if l1.val < current_l2_node.val:
            l1.next = l2
            return l1
        elif l1.val > current_l2_node.val:
            l2.next = l1
            l2_next = l2.next
            l1.next = l2_next
            l2.next = l1
            return l2
    elif not l2.next:
        current_l1_node = l1

        # Go to end of list
        while current_l1_node.next:
            if current_l1_node.next.val > l2.val:
                break
            current_l1_node = current_l1_node.next

        if current_l1_node.val < l2.val:
            current_l1_node.next = l2
            return l1
        elif current_l1_node.val > l2.val:
            l2_next = l2.next
            l1.next = l2_next
            l2.next = l1
            return l2

    merged_list_head = None
    merged_list = merged_list_head
    l1_current_node = l1
    l2_current_node = l2

    while l1_current_node and l2_current_node:
        if l1_current_node.val == l2_current_node.val:

            if merged_list:
                merged_list.next = l1_current_node
            else:
                merged_list_head = l1_current_node 

            merged_list = l1_current_node
            l1_current_node = l1_current_node.next
                
        elif l1_current_node.val > l2_current_node.val:
            merged_list.next = l2_current_node
            merged_list = l2_current_node
            l2_current_node = l2_current_node.next

        elif l1_current_node.val < l2_current_node.val:
            merged_list.next = l1_current_node
            merged_list = l1_current_node
            l1_current_node = l1_current_node.next

    if l1_current_node:
        merged_list.next = l1_current_node
    elif l2_current_node:
        merged_list.next = l2_current_node

    return merged_list_head

# print(mergeTwoLists(ListNode(), list_to_singly_linked_list([0])))
print(mergeTwoLists(list_to_singly_linked_list([0, 2, 4, 9]), list_to_singly_linked_list([0, 2, 4, 9])))
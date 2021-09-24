from typing import List, Optional
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
    merged_list_head = None
    merged_list = merged_list_head
    l1_current_node = l1
    l2_current_node = l2

    while l1_current_node and l2_current_node:
        if l1_current_node.val == l2_current_node.val:
            print("SAMEL", "l1",l1_current_node, "l2",l2_current_node)
            new_nodes = ListNode(l1_current_node.val, ListNode(l2_current_node.val))
            
            merged_list.next = new_nodes
            merged_list = new_nodes.next
            print("mergedd", merged_list)
            l2_current_node = l2_current_node.next
            l1_current_node = l1_current_node.next

        elif l1_current_node.val > l2_current_node.val:
            print("l1 is more:", l1_current_node)
            print("mergedd", merged_list)
            merged_list.next = l2_current_node
            merged_list = l2_current_node
            l2_current_node = l2_current_node.next

        elif l1_current_node.val < l2_current_node.val:
            print("l1 is less:", l1_current_node)
            print("mergedd", merged_list)
            merged_list.next = l1_current_node
            merged_list = l1_current_node
            l1_current_node = l1_current_node.next
        print("CURRENT MERGERD SHIT", merged_list_head)

    print(merged_list)
    return merged_list_head
print(mergeTwoLists(ListNode(), list_to_singly_linked_list([0])))
# print(mergeTwoLists(list_to_singly_linked_list([1,2,4]), list_to_singly_linked_list([1,3,4])))
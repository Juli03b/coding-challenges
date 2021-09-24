from data_structures.singly_linked_list import ListNode
from typing import Any, List

def list_to_linked_list(list_to_convert: List[Any]):
    head = ListNode(list_to_convert[0])
    current_node = head
    for val in list_to_convert[1:]:
        new_node = ListNode(val)
        current_node.next = new_node
        current_node = new_node
    return head
        

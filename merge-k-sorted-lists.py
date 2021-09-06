# LINK TO LEETCODE: https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional

# Incomplete

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to check if min exists in a linked list
def check_min(min: int, list_node):
    while list_node:
        if list_node.val == min:
            return list_node.val
        elif list_node.next:
            list_node = list_node.next
        else:
            return False

def mergeKList(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.

    Example 1:

        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6

    Example 2:
        
        Input: lists = []
        Output: []
        Example 3:
        
        Input: lists = [[]]
        Output: []
    """
    current_list_node = ListNode()
    sorted_linked_list = ListNode()
    # loop through all list nodes in list of linked lists
    for i in range(len(lists)):
        #get a starting node
        lowest_node = lists[i]

        #loop through other lists to find a lower value
        for j in range(i, len(lists)):
            # get current node 
            current_node = lists[j]
            # traverse through list nodes
            while current_node:
                low = check_min(current_list)
                #check if there is a lower value
                if low and low < lowest_node.val:
                    lowest_node = current_list
                    break
                # set the next node if no lower value found
                current_node = current_node.next
        
        current_list_node = lowest_node
        sorted_linked_list = lowest_node

        if sorted_linked_list.next:
            sorted_linked_list.next = lowest_node
            current_list_node.next = lowest_node  
            
    return sorted_linked_list

print()
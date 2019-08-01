from singly_linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            # Empty list
            return None
        rest_of_list = head.next
        if rest_of_list:
            # More than 1 node
            # Find the new head for the rest of the list
            new_head = self.reverseList(rest_of_list)
            # Make the new tail of the rest of the list points at the original head
            head.next.next = head
            # Make the original head the new tail for the whole list
            head.next = None
            # Return the new head
            return new_head
        else:
            # Only 1 node
            return head

    def reverseList_iterative(self, head: ListNode) -> ListNode:
        if not head:
            # Empty list
            return None
        
        current_node = head.next
        prev_node = head

        if current_node is None:
            # Only 1 node
            return head

        while current_node.next is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        current_node.next = prev_node
        head.next = None
        return current_node
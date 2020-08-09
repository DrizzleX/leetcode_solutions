"""
1.1 Reverse linked list
"""
from ll_util import *


def reverse_ll_recursion(head):
    if head.next is None:
        # Only 1 node
        return head
    second_node = head.next
    new_head = reverse_ll_recursion(second_node)
    second_node.next = head
    head.next = None
    return new_head


def reverse_ll(head):
    if head.next is None:
        return head
    prev_node = head
    current_node = head.next
    while current_node.next is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    current_node.next = prev_node
    head.next = None
    return current_node


def reverse_print_ll(head):
    if head.next:
        reverse_print_ll(head.next)
    print(head.data)


print('A linkedlist with 1 nodes')
n1 = build_ll([1])
print_ll(n1)
#reversed_ll = reverse_ll_recursion(n1)
reversed_ll = reverse_ll(n1)
print_ll(reversed_ll)
reverse_print_ll(reversed_ll)

print('A linkedlist with 2 nodes')
n1 = build_ll([1,2])
print_ll(n1)
#reversed_ll = reverse_ll_recursion(n1)
reversed_ll = reverse_ll(n1)
print_ll(reversed_ll)
reverse_print_ll(reversed_ll)

print('A linkedlist with 5 nodes')
n1 = build_ll([1,2,3,4,5])

print_ll(n1)
#reversed_ll = reverse_ll_recursion(n1)
reversed_ll = reverse_ll(n1)
print_ll(reversed_ll)
reverse_print_ll(reversed_ll)


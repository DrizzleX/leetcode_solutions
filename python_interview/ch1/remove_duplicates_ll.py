import random
from ll_util import *


def remove_duplicates_recursion(head):
    if head is None or head.next is None:
        return head
    second_node = head.next
    # Use recursion to remove the duplicates in the rest of the list
    rest_list = remove_duplicates_recursion(second_node)
    # Go over the rest of the list, if there is a duplicate of the head, remove it (because we want to maintain the
    # order)
    curr_node = rest_list
    prev_node = head
    while curr_node is not None:
        if head.data == curr_node.data:
            prev_node.next = curr_node.next
            # We know the rest of the list already contains unique values, once we've found one duplicate,
            # we can break
            break
        # Move to the next node to search for duplicate
        prev_node = curr_node
        curr_node = curr_node.next
    return head


def remove_duplicates_hash(head):
    if head is None or head.next is None:
        return head
    seen_values = {head.data}
    prev_node = head
    curr_node = head.next
    while curr_node is not None:
        if curr_node.data in seen_values:
            curr_node = curr_node.next
            # Remove the node from the list
            prev_node.next = curr_node
        else:
            seen_values.add(curr_node.data)
            prev_node = curr_node
            curr_node = curr_node.next
    return head


def remove_duplicates_iterative(head):
    outer_current = head
    while outer_current:
        prev_node = outer_current
        curr_node = outer_current.next
        while curr_node:
            # Go through the remaining list to check duplicates
            if curr_node.data == outer_current.data:
                curr_node = curr_node.next
                # Remove the duplicate node from the list
                prev_node.next = curr_node
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        # Move the outer pointer to next node
        outer_current = outer_current.next
    return head


for each in [
    [1],
    [1, 2],
    [1, 1],
    [random.randint(1, 10) for each in range(5)],
    [random.randint(1, 10) for each in range(20)]
]:
    head = build_ll(each)
    print_ll(head, message="Before: ", end='')
    #head = remove_duplicates_recursion(head)
    #head = remove_duplicates_hash(head)
    head = remove_duplicates_iterative(head)
    print_ll(head, message="After: ", end='')

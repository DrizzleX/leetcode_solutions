from ll_util import *


def add_num_ll(head1, head2):
    head = None
    prev_node = None
    carry = 0
    # Classic head1 & head2, head1, and head2. 3-section processing
    while head1 and head2:
        new_node = LNode(0)
        if prev_node is not None:
            prev_node.next = new_node
        if head is None:
            # Only execute once. Must follow the previous if
            # because prev_node is assigned here
            head = new_node
        prev_node = new_node
        new_node.data = (head1.data + head2.data + carry) % 10
        carry = (head1.data + head2.data + carry) // 10
        head1 = head1.next
        head2 = head2.next

    while head1:
        new_node = LNode(0)
        if prev_node is not None:
            prev_node.next = new_node
        if head is None:
            head = new_node
        prev_node = new_node
        new_node.data = (head1.data + carry) % 10
        carry = (head1.data + carry) // 10
        head1 = head1.next

    while head2:
        new_node = LNode(0)
        if prev_node is not None:
            prev_node.next = new_node
        if head is None:
            head = new_node
        prev_node = new_node
        new_node.data = (head2.data + carry) % 10
        carry = (head2.data + carry) // 10
        head2 = head2.next

    if carry != 0:
       new_node = LNode(carry)
       prev_node.next = new_node

    return head


for pair in [
    ([], []),
    ([1], []),
    ([1], [9]),
    ([1, 2, 3], []),
    ([1, 2, 3], [4, 8, 6]),
    ([3, 1, 5], [5, 9, 2]),
    ([1], [9, 9, 9]),
]:
    head1 = build_ll(pair[0])
    head2 = build_ll(pair[1])
    head = add_num_ll(head1, head2)
    print_ll(head)



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


def make_linked_list(vals):
    """
    Make a singly linked list and return the head
    """
    if not vals:
        return None
    prev_node = ListNode(vals[0])
    head_node = prev_node
    for val in vals[1:]:
        node = ListNode(val)
        prev_node.next = node
        prev_node = node

    return head_node


def find_node(linked_list, val):
    """
    Find a node holding the specified value in a linked list and return the node.
    Return None if this value does not exist
    """
    head_node = linked_list
    while head_node is not None:
        if head_node.val == val:
            return head_node
        else:
            head_node = head_node.next

    return head_node


def print_linked_list(linked_list):
    """
    Print values in a linked list, separated by a space
    """
    head_node = linked_list
    while head_node is not None:
        if head_node.next is not None:
            print(head_node.val, end=' ')
        else:
            print(head_node, end='\n')
        head_node = head_node.next


def linked_list_as_list(linked_list):
    """
    Return the values in a linked list as a Python list
    """
    result = []
    head_node = linked_list
    while head_node is not None:
        result.append(head_node.val)
        head_node = head_node.next

    return result

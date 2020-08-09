class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def build_ll(vals):
    head = None
    prev = None
    if not vals:
        return head
    for idx, v in enumerate(vals):
        node = LNode(v)
        if idx == 0:
            head = node
        else:
            prev.next = node
        prev = node

    return head

def print_ll(head):
    n = head
    while n.next is not None:
        print('{}->'.format(n.data), end='')
        n = n.next
    print(n.data)

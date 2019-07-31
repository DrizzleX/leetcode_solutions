import pytest
from delete_node_in_a_linked_list import Solution
from singly_linked_list import ListNode, make_linked_list, find_node, print_linked_list, linked_list_as_list

test_data_set = [
    ([1, 2, 54, 22, 3, 4], 3, [1, 2, 54, 22, 4]),
    ([4, 5, 19], 5, [4, 19]),
    ([2, 3], 2, [3])
]

@pytest.mark.parametrize("vals, target, expected", test_data_set)
def test_solution(vals, target, expected):
    solution = Solution()
    linked_list = make_linked_list(vals)
    target_node = find_node(linked_list, target)
    print_linked_list(linked_list)
    solution.deleteNode(target_node)
    print_linked_list(linked_list)
    assert linked_list_as_list(linked_list) == expected
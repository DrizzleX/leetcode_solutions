import pytest
from reverse_linked_list import Solution
from singly_linked_list import make_linked_list, print_linked_list, linked_list_as_list

test_data_set = [
    ([1, 2, 3, 4], [4, 3, 2, 1]),
    ([1, 2, 3], [3, 2, 1]),
    ([1, 2], [2, 1]),
    ([1], [1]),
]


@pytest.mark.parametrize("values, expected", test_data_set)
def test_reverse_list(values, expected):
    solution = Solution()
    linked_list = make_linked_list(values)
    print_linked_list(linked_list)
    reversed_list = solution.reverseList(linked_list)
    print_linked_list(reversed_list)
    assert linked_list_as_list(reversed_list) == expected


@pytest.mark.parametrize("values, expected", test_data_set)
def test_reverse_list_iterative(values, expected):
    solution = Solution()
    linked_list = make_linked_list(values)
    print_linked_list(linked_list)
    reversed_list = solution.reverseListIterative(linked_list)
    print_linked_list(reversed_list)
    assert linked_list_as_list(reversed_list) == expected
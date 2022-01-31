import sys, os
from enum import Enum, auto
from os.path import dirname, abspath, join
import argparse


class DataStructure(Enum):
    LIST = 'list'
    LINKEDLIST = 'linkedlist'

def main(q_no, q_title, method_signature, data_structures=None):
    if data_structures == None:
        data_structures = []
    par_dir = abspath(dirname(__file__))

    answer_dir = join(par_dir, f'{q_no}_{q_title}')
    answer_file = '{}.py'.format(q_title)
    try:
        os.mkdir(answer_dir)
    except FileExistsError:
        pass
    data_structure_to_imports = {
        DataStructure.LIST: 'from typing import List',
        DataStructure.LINKEDLIST: 'from singly_linked_list import ListNode, make_linked_list, print_linked_list, linked_list_as_list'
    }
    data_structure_imports = '\n'.join([data_structure_to_imports[ds] for ds in data_structures])

    with open(os.path.join(answer_dir, answer_file), 'w') as f:
        content = f"""import pytest
{data_structure_imports}


class Solution:
    def {method_signature}:
        pass


test_data_set = [
]


@pytest.mark.parametrize('', test_data_set)
def test_solution():
    solution = Solution()
        """.format(method_signature)
        f.write(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Leetcode answer template')
    # e.g. 9. Palindrome Number
    parser.add_argument('question_title', help='The full title of the question')
    # e.g. isPalindrome(self, x: int) -> bool
    parser.add_argument('method_signature', help='The signature of the method (without def keyword)')
    parser.add_argument('--data-structures', help='Avaialble data structures: list, linkedlist')
    args = parser.parse_args()


    original_title = args.question_title
    method_signature = args.method_signature
    if args.data_structures:
        data_structures = [DataStructure(each) for each in args.data_structures.split(',')]
    else:
        data_structures = []

    original_title_array = original_title.split('. ')
    q_no = original_title_array[0]
    q_title = original_title_array[1].lower().replace(' ', '_')

    main(q_no, q_title, method_signature, data_structures)

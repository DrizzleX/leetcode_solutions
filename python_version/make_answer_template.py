import sys, os
from enum import Enum, auto


class DataStructure(Enum):
    List = auto()
    LinkedList = auto()

def main(q_no, q_title, method_signature, data_structures=None):
    if data_structures == None:
        data_structures = []
    answer_dir = '{}_{}'.format(q_no, q_title)
    answer_file = '{}.py'.format(q_title)
    try:
        os.mkdir(answer_dir)
    except FileExistsError:
        pass
    data_structure_to_imports = {
        DataStructure.List: 'from typing import List',
        DataStructure.LinkedList: 'from singly_linked_list import ListNode, make_linked_list, print_linked_list, linked_list_as_list'
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
    if len(sys.argv) != 3:
        print('Usage: {} question_title method_signature'.format(sys.argv[0]))

    original_title = sys.argv[1]
    method_signature = sys.argv[2]

    original_title_array = original_title.split('. ')

    q_no = original_title_array[0]
    q_title = original_title_array[1].lower().replace(' ', '_')
    main(q_no, q_title, method_signature, [DataStructure.List, DataStructure.LinkedList])

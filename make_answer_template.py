#!/bin/env python

import sys, os

def main(q_no, q_title, method_signature):
    answer_dir = '{}_{}'.format(q_no, q_title)
    answer_file = '{}.py'.format(q_title)
    os.mkdir(answer_dir)

    with open(os.path.join(answer_dir, answer_file), 'w') as f:
        content = """#!/bin/env python
class Solution:
    def {}:
        pass
        """.format(method_signature)
        f.write(content)


    with open(os.path.join(answer_dir, 'test_{}'.format(answer_file)), 'w') as f:
        content = """#!/bin/env python
import pytest
from {} import Solution

test_data_set = [
]

@pytest.mark.parametrize("", test_data_set)
def test_solution():
    solution = Solution()
        """.format(q_title)
        f.write(content)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} question_title method_signature'.format(sys.argv[0]))

    original_title = sys.argv[1]
    method_signature = sys.argv[2]

    original_title_array = original_title.split('. ')

    q_no = original_title_array[0]
    q_title = original_title_array[1].lower().replace(' ', '_')
    main(q_no, q_title, method_signature)

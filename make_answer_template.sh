#!/bin/bash

if [ $# != 2 ];
then
    echo "Usage: $0 question_title method_signature"
else
    original_title=$1
    method_signature=$2
    echo "Start to generate answer template for ${original_title}"
    IFS='.'
    read -a original_title_array <<< ${original_title}
    q_no=${original_title_array[0]}
    q_title=${original_title_array[1]}
    echo ${q_no}
    echo ${q_title}
fi

exit 1


answer_dir=${q_no}_${q_title}
answer_file=${q_title}.py

mkdir ${answer_dir}
echo "
class Solution:
    def ${method_signature}:
        pass
" > ${answer_dir}/${answer_file}


echo "
import pytest
from ${q_title} import Solution

test_data_set = [
]

@pytest.mark.parametrize("", test_data_set)
def test_solution():
    solution = Solution()
" > ${answer_dir}/test_${answer_file}

# I need to test the code in a02.py:
# Using pytest to test the code in a02.py:

import pytest
from a02 import get_multistringmatching, create_output_file

def test_multistringmatching():
    result1 = get_multistringmatching('Assignment02/stringmultimatching.in')
    create_output_file(result1, 'Assignment02/my_stringmultimatching_test.ans')
    read_file_test = open('Assignment02/my_stringmultimatching_test.ans', 'r')
    read_file_ans = open('Assignment02/my_stringmultimatching.ans', 'r')
    read_file_test = read_file_test.readlines()
    print("read_file_test: ", read_file_test)
    read_file_ans = read_file_ans.readlines()
    print("read_file_ans: ", read_file_ans)
    print("read_file_test == read_file_ans: ", read_file_test == read_file_ans)
    assert read_file_test == read_file_ans

test_multistringmatching()

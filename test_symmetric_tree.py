import pytest
from symmetric_tree import is_symmetric
from Util import create_tree_from_array


use_cases = (
    ([1, 2, 2, 3, 4, 4, 3, 5, None, None, None, None, None, None, 5], True),
    ([5, 6, 7, 8, 9, 3, None], False)
)

edge_cases = (
    ([1], True),
    ([1, 2, 2, 3, None, None, 3], True)
)


@pytest.mark.parametrize(('input_array', 'expected'), use_cases+edge_cases)
def test_is_symmetric(input_array, expected):
    root_input = create_tree_from_array(input_array)
    assert is_symmetric(root_input) == expected

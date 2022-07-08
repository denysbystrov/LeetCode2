import pytest
from Util import create_tree_from_array
from maximum_depth import maximum_depth


use_cases = (
    ([1, 2, 3, 4, 5, 6, 7], 3),
    ([1, 2, None, 3, 4, None, None, None, None, 5, 6, None, None, 7], 4)
)

edge_cases = (
    ([], 0),
    ([1], 1),
    ([1, 2, None, 3], 3)
)


@pytest.mark.parametrize(('input_array', 'expected'), use_cases+edge_cases)
def test_maximum_depth(input_array, expected):
    root_input = create_tree_from_array(input_array)
    assert maximum_depth(root_input) == expected

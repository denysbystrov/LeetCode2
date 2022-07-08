import pytest
from sorted_array_to_tree import sorted_array_to_bst
from Util import check_tree_height_balanced


use_cases = (
    ([1, 2, 3, 4, 5]),
    ([-10, -9, 2, 7, 10, 11])
)

edge_cases = (
    ([]),
    ([1])
)


@pytest.mark.parametrize('input_array', use_cases+edge_cases)
def test_sorted_array_to_bst(input_array):
    assert check_tree_height_balanced(sorted_array_to_bst(input_array)) is not None

import pytest
from intersection_lists import get_intersection_node
from Util import create_two_lists


use_cases = (
    ([1, 2, 3, 4, 5], [6, 7, 8], 2),
    ([2, 6, 4], [3, 5], -1)
)

edge_cases = (
    ([], [], -1),
    ([1], [], -1),
    ([1], [2], 0)
)


@pytest.mark.parametrize(('arr_a', 'arr_b', 'intersect_idx'), use_cases+edge_cases)
def test_get_intersection_node(arr_a, arr_b, intersect_idx):
    head_a, head_b, expected = create_two_lists(arr_a, arr_b, intersect_idx)
    assert get_intersection_node(head_a, head_b) == expected

import pytest
from cycle_list import has_cycle
from Util import create_list_from_array

use_cases = (
    ([1, 2, 3, 4], -1, False),
    ([1, 2, 3, 4], 0, True),
    ([2, 2, 2], 1, True)
)

edge_cases = (
    ([1], -1, False),
    ([1, 2], 0, True)
)


@pytest.mark.parametrize(('list_array', 'cycle_index', 'expected'), use_cases+edge_cases)
def test_has_cycle(list_array, cycle_index, expected):
    head_node = create_list_from_array(list_array, cycle_index)
    assert has_cycle(head_node) == expected

import pytest
from Util import create_tree_from_array
from binary_tree_in_order import in_order_traversal

use_cases = (
    (1, {1: [3, 6], 3: [4, 5], 6: [None, 7], 4: [None, None], 5: [None, None], 7: [None, None]}, [4, 3, 5, 1, 6, 7]),
    (2, {2: [4, 5], 4: [6, None], 6: [7, None], 7: [None, None], 5: [3, 1], 3: [None, None], 1: [None, None]},
     [7, 6, 4, 2, 3, 5, 1])
)

edge_cases = (
    (None, None, []),
    (1, {1: [None, None]}, [1])
)


@pytest.mark.parametrize(('root_num', 'node_dict', 'expected'), use_cases+edge_cases)
def test_in_order_traversal(root_num, node_dict, expected):
    input_root_node = create_tree_from_array(root_num, node_dict)
    assert in_order_traversal(input_root_node) == expected

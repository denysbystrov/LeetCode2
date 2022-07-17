import pytest
from single_number import single_number


use_cases = (
    ([2, 2, 1, 1, 3], 3),
    ([111, 0, 0, 111, 4, 3, 3, 5, 4], 5)
)

edge_cases = (
    ([2], 2),
    ([2, 1, 2], 1)
)


@pytest.mark.parametrize(('input_nums', 'expected'), use_cases+edge_cases)
def test_single_number(input_nums, expected):
    assert single_number(input_nums) == expected

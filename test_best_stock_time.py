import pytest
from best_stock_time import max_profit


use_cases = (
    ([7, 1, 3, 4, 7, 2, 5], 6),
    ([4, 3, 2, 1, 0], 0),
    ([2, 1, 2, 0, 1], 1)
)

edge_cases = (
    ([1], 0),
    ([1, 2], 1),
    ([2, 1], 0),
    ([3, 3, 3], 0)
)


@pytest.mark.parametrize(('input_prices', 'expected'), use_cases+edge_cases)
def test_max_profit(input_prices, expected):
    assert max_profit(input_prices) == expected


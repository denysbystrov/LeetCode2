import pytest
from pascal_traingle import generate


test_cases = (
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    (1, [[1]])
)


@pytest.mark.parametrize(('num_rows', 'expected'), test_cases)
def test_generate(num_rows, expected):
    assert generate(num_rows) == expected

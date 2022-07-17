import pytest
from valid_palindrome import is_palidrome


use_cases = (
    ("A man, a plan, a canal: Panama", True),
    ('xfgddefddgfx', False),
    ('6ghf6: , fdsaf', False)
)

edge_cases = (
    (' ', True),
    (' a :', True),
    (':/ a/:: f', False)
)


@pytest.mark.parametrize(('input_s', 'expected'), use_cases+edge_cases)
def test_is_palidrome(input_s, expected):
    assert is_palidrome(input_s) == expected


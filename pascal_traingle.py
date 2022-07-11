"""Number 118: Pascal's Traingle"""
from typing import List


def generate(num_rows: int) -> List[List[int]]:
    pascal_traingle = [[1]]
    while len(pascal_traingle) < num_rows:
        num_components = len(pascal_traingle) + 1
        new_row = []
        for i in range(num_components):
            left_val = 0 if i-1 < 0 else pascal_traingle[-1][i-1]
            right_val = 0 if i >= len(pascal_traingle[-1]) else pascal_traingle[-1][i]
            new_row.append(left_val+right_val)
        pascal_traingle.append(new_row)

    return pascal_traingle

from typing import List


def rotate_matrix_90(array: List[List[int]]):
    """2차원 리스트(행렬)를 90도로 회전하는 메서드"""
    row_length = len(array)
    column_length = len(array[0])

    result = [[0] * row_length for _ in range(column_length)]

    for r in range(row_length):
        for c in range(column_length):
            result[c][row_length - 1 - r] = array[r][c]

    return result


array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(f"Original Matrix    : {array}")
print(f"Rotate by 90 degree: {rotate_matrix_90(array)}")

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:      # 종료 조건: 원소가 1개인 경우 종료
        return

    pivot = start         # 호어 분할: 피벗은 첫 번째 원소의 인덱스
    left = start + 1      # 왼쪽 인덱스부터는 피벗보다 큰 데이터의 인덱스를 찾기 시작하고,
    right = end           # 오른쪽 인덱스부터는 피벗보다 작은 데이터의 인덱스를 찾기 시작함

    # Part 1: 분할 - 한 배열 내에서 계속해서 교환해야 하므로,
    while left <= right:
        # 왼쪽에서는 피벗보다 큰 데이터의 인덱스를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1         # 찾을 때까지 왼쪽 인덱스를 오른쪽으로 한 칸씩 이동

        # 오른쪽에서는 피벗보다 작은 데이터의 인덱스를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1        # 찾을 때까지 오른쪽 인덱스를 왼쪽으로 한 칸씩 이동

        # 만약 엇갈렸다면 피벗과 작은 데이터의 값을 교체한다.
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 만약 엇갈리지 않았다면 작은 데이터의 값과 큰 데이터의 값을 바꾼다.
        else:
            array[left], array[right] = array[right], array[left]

    # Part 2: 분할 이후 왼쪽 부분에서 재귀적으로 정렬 수행
    quick_sort(array, start, right - 1)

    # Part 3: 분할 이후 오른쪽 부분에서 재귀적으로 정렬 수행
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

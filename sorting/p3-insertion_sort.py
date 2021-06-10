def insertion_sort(array):
    # 삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에,
    # 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
    # 따라서 인덱스 1 부터 정렬을 시작한다.
    for i in range(1, len(array)):
        for j in range(i, 0, -1):  # 인덱스 i 부터 1 까지 감소하며 이동
            if array[j] < array[j - 1]:  # 이동 중에 현재 값이 앞의 값보다 작다면,
                array[j], array[j - 1] = array[j - 1], array[j]
            # 선택 정렬은 현재 데이터의 그 앞까지의 데이터는 이미 정렬되어 있다고 가정하므로,
            # 자기보다 작은 값을 만나면 더 이상 앞으로 탐색하지 않아도 되므로 그 위치에서 멈춤
            else:
                break

    return array


array = [5, 2, 3, 7, 8, 1, 0, 4, 9, 6]
print(f"Original List       : {array}")
print(f"After Insertion Sort: {insertion_sort(array)}")

import heapq


def heap_sort(array):
    '''O(nlogn)'''
    min_heap_list = []
    result = []

    # 힙에 넣을 때 힙 구조에 맞게 삽입됨
    for val in array:
        heapq.heappush(min_heap_list, val)

    # 힙에 삽입된 모든 원소를 최소힙 구조로 꺼내어 담기
    for _ in range(len(min_heap_list)):
        result.append(heapq.heappop(min_heap_list))

    return result


array = [5, 2, 3, 7, 8, 1, 0, 4, 9, 6]
print(f"Original List  : {array}")
print(f"After Heap Sort: {heap_sort(array)}")


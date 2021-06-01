import heapq


def heap_sort(array):
    max_heap_list = []
    result = []

    for val in array:
        heapq.heappush(max_heap_list, -val)

    for _ in range(len(max_heap_list)):
        result.append(-heapq.heappop(max_heap_list))

    return result


array = [5, 2, 3, 7, 8, 1, 0, 4, 9, 6]
print(f"Original List  : {array}")
print(f"After Heap Sort: {heap_sort(array)}")

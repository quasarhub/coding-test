import heapq


def dijkstra(graph, start):
    # 각각의 키에 대한 값을 무한으로 초기화
    distances = {node: float('inf') for node in graph}
    # 처음 시작할 때 자기 자신까지의 거리는 0
    distances[start] = 0
    # 모든 정점이 저장될 큐를 생성
    queue = []
    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start], start])

    while queue:
        # minheap 방식으로 인해 가장 작은 값이 먼저 나옴
        current_distance, current_node = heapq.heappop(queue)

        # 만약 지금까지 업데이트된 거리가 해당 노드까지의 거리보다 작다면 계산할 필요 없다.
        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            # 먼저 각 노드에서 이웃노드까지의 거리를 합한 다음
            distance = current_distance + weight

            # 만약 해당 배열에 있는 거리 보다 지금 거리가 작다면 최단거리이므로 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                # minheap 구조에 맞게 알아서 정렬하여 들어감
                heapq.heappush(queue, [distance, adjacent])

    return distances


my_graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

# {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
print(dijkstra(my_graph, 'A'))

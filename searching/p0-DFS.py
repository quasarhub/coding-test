def dfs(graph, v, visited):
    visited[v] = True    # 현재 노드를 방문 처리
    print(v, end=' ')    # 현재 방문한 노드 출력

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문: 스택 자료구조 이용
    for i in graph[v]:
        if not visited[i]:          # 이웃한 노드 중 방문한 노드가 없다면
            dfs(graph, i, visited)  # 재귀적(스택 이용)으로 방문


# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 각 노드가 연결된 정보를 인접 행렬(리스트 자료형)로 표현(2차원 리스트)
graph = [
    [],                 # 0 번째 노드는 없으므로 인접 노드도 없다.
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

dfs(graph, 1, visited)

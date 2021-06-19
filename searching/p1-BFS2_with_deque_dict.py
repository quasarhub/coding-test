from collections import deque


def bfs(graph, start_node):
    visited = []
    need_visit = deque()

    # 1. 어디서 부터 시작할지 need_visit 에 넣고 시작한다.
    need_visit.append(start_node)

    # 더이상 방문할 노드가 없을 때까지
    while need_visit:
        # need_visit 데크에서 가장 앞에 있는 노드를 뽑아옴
        node = need_visit.popleft()

        # need_visit 에서 빼온 노드가 아직 방문하지 않은 노드라면,
        if node not in visited:
            # 이제 해당 노드는 방문했으므로 visited 리스트에 해당 노드를 넣고,
            visited.append(node)
            # 그 해당 노드의 values, 즉 연결된 노드를 need_visit 에 넣는다.
            need_visit.extend(graph[node])

    # BFS는 최종적으로 visited 에 있는 순서대로 방문한다.
    return visited


graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# Output should be: ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
print(bfs(graph, 'A'))
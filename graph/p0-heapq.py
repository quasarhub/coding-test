import heapq

queue = []
heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])

# [[1, 'C'], [5, 'B'], [2, 'A'], [7, 'D']]
print(queue)

# [1, 'C']
# [2, 'A']
# [5, 'B']
# [7, 'D']
for i in range(len(queue)):
    print(heapq.heappop(queue))


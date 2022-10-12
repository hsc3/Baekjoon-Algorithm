# [6118] 숨바꼭질 | Silver 1 | https://www.acmicpc.net/problem/6118
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [0, 0] + [float("inf")] * (N-1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque([1]) # BFS
while queue:
    u = queue.popleft()
    for v in graph[u]:
        if distance[v] == float("inf"):
            distance[v] = distance[u] + 1
            queue.append(v)

maximum_distance = max(distance)
print(distance.index(maximum_distance), maximum_distance, distance.count(maximum_distance))



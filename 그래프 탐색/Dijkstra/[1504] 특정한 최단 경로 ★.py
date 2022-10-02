# [1504] 특정한 최단 경로 | Gold 4 | https://www.acmicpc.net/problem/1504
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
# (1 -> v1) + (v1 -> v2) + (v2 -> N) 최단 경로와 (1 -> v2) + (v2 -> v1) + (v1 -> N) 최단 경로를 비교

def Dijkstra(start):

    cost = [float("inf") for _ in range(N+1)]
    cost[start] = 0

    heap = []
    heappush(heap, [0, start])
    while heap:
        distance, u = heappop(heap)
        if cost[u] < distance:
            continue

        for nextDistance, v in graph[u]:
            if distance + nextDistance < cost[v]:
                cost[v] = distance + nextDistance
                heappush(heap, [cost[v], v])

    return cost

answer = float("inf")
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

v1, v2 = map(int, input().split())  # 반드시 지나야하는 정점
path1 = Dijkstra(1) # 1에서 시작하는 최단 경로
pathV1 = Dijkstra(v1) # v1에서 시작하는 최단 경로
pathV2 = Dijkstra(v2) # v2에서 시작하는 최단 경로

answer = min(path1[v1] + pathV1[v2] + pathV2[N], path1[v2] + pathV2[v1] + pathV1[N])
print(answer if answer != float("inf") else -1)
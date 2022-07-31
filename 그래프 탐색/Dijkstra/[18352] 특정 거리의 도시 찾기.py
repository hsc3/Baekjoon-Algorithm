# [18352] 특정 거리의 도시 찾기 | Silver 2 | 그래프 (Dijkstra)
'''
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
'''
import heapq
import sys; input = sys.stdin.readline

N, M, K, X = map(int, input().split()) # 도시의 수, 도로의 수, 거리 정보, 출발 도시의 번호
graph = [[] for _ in range(N+1)]
distance = [float("inf") for _ in range(N+1)]
distance[X] = 0
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

heap = []
heapq.heappush(heap, [distance[X], X])

while heap:
    distanceToCity, city = heapq.heappop(heap) # 최단 경로의 도시를 선택합니다.
    for adj in graph[city]: # 해당 도시로부터 인접한 도시들의 거리를 업데이트합니다.
        if distanceToCity + 1 < distance[adj]:
            distance[adj] = distanceToCity + 1
            heapq.heappush(heap, [distance[adj], adj])

if K not in distance:
    print(-1)
else:
    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
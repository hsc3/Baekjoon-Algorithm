# [1753] 최단 경로 | Gold 4 | 그래프 (Dijkstra)
'''
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
'''
import sys, heapq, math
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append([w, v]) # 가중치와 간선을 저장합니다.
    
distance = [math.inf for _ in range(V+1)]
distance[K] = 0

heap = []
heapq.heappush(heap, [0, K])

while heap :
    weight_to_vertex, vertex = heapq.heappop(heap) # 정점까지의 거리, 최단 경로의 정점
    for weight_to_adjacent, adjacent in graph[vertex] :
        if weight_to_vertex + weight_to_adjacent < distance[adjacent] : # 정점을 기준으로 인접 정점의 최단 경로를 갱신
            distance[adjacent] = weight_to_vertex + weight_to_adjacent
            heapq.heappush(heap, [distance[adjacent], adjacent])

for i in distance[1:] :
    print(i) if i != math.inf else print("INF")
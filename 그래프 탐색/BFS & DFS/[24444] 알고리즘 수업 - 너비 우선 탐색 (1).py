'''
[24444] 알고리즘 수업 - 너비 우선 탐색 (1) / Silver 2 / 그래프
N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다.
정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    for each v ∈ V - {R}
        visited[v] <- NO;
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while (Q ≠ ∅) {
        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
            if (visited[v] = NO) then {
                visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
                enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
            }
    }
}
'''
import sys
input = sys.stdin.readline
from collections import deque


def BFS(r):
    global visitOrder
    q = deque([r])

    while q:
        v = q.popleft()
        if not visited[v]: # 아직 방문하지 않은 정점일 경우, 해당 정점의 방문 순서 표시
            visited[v] = True
            answer[v] = visitOrder
            visitOrder += 1

            for adj in sorted(graph[v]): # 인접한 모든 정점을 저장
                q.append(adj)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)
visitOrder = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

BFS(r)
print(*answer[1:], sep = '\n')
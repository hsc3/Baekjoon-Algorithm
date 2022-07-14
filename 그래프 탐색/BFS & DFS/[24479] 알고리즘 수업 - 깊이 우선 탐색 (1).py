'''
[24479] 알고리즘 수업 - 깊이 우선 탐색 (1) / Silver 2 / 그래프
N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다.
정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.
(i번째 줄에는 정점 i의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.)
깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def DFS(r):
    global visitOrder

    # 방문 순서를 표시
    visited[r] = True
    answer[r] = visitOrder
    visitOrder += 1

    # 인접한 방문하지 않은 정점을 방문 (오름차순)
    for adj in sorted(graph[r]):
        if not visited[adj]:
            DFS(adj)
    return


n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1) # 방문 순서를 저장
visitOrder = 1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(r)
print(*answer[1:], sep='\n')
'''
[1260] DFS와 BFS | Silver 2 | 그래프 (DFS, BFS)
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
(단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.)
'''
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
adjacent = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M) :
    start, end = map(int, input().split())
    adjacent[end].append(start) # 양방향
    adjacent[start].append(end)

DFS = []
BFS = []

# DFS : 깊이우선탐색 -> Stack 활용
stack = []
stack.append(V) # 탐색의 시작 정점 삽입
while stack :
    v = stack.pop()
    if visited[v] == False :
        DFS.append(v)
        visited[v] = True # 방문
    # 인접 정점 탐색 - 스택이기 때문에 높은 숫자의 정점부터 확인
    for a in sorted(adjacent[v], reverse = True) : 
        if visited[a] == False : # 방문하지 않은 경우, 스택에 넣는다
            stack.append(a)

# BFS : 너비우선탐색 -> queue 활용
visited = [False] * (N+1)
queue = []
queue.append(V)
while queue :
    v = queue.pop(0)
    if visited[v] == False :
        BFS.append(v)
        visited[v] = True # 방문
        # 인접 정점 탐색 - 큐이기 때문에 낮은 숫자의 정점부터 확인
        for a in sorted(adjacent[v]) :
            if visited[a] == False : # 방문하지 않은 경우, 큐의 뒤에 넣는다
                queue.append(a)
print(*DFS)
print(*BFS)

'''
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N+1):
    graph[i].sort()

def dfs(graph, v, visited_dfs): # 깊이우선탐색은 재귀적으로 구현할 수 있다.
    visited_dfs[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

def bfs(graph, v, visited_bfs):
    list = []
    list.append(v)
    visited_bfs[V] = True

    while len(list) :
        v = list.pop(0)
        print(v, end = ' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                list.append(i)
                visited_bfs[i] = True

dfs(graph, V, visited_dfs)
print('', sep = '\n')
bfs(graph, V, visited_bfs)
'''
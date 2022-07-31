'''
[11742] 연결 요소의 개수 | Silver 2 | 그래프 (DFS)
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(i) :
    visited[i] = True
    for a in adj[i] :
        if visited[a] == False :
            DFS(a)

n, m = map(int, input().split()) # 정점의 갯수, 간선의 갯수
adj = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m) :
    s, e = map(int, input().split()) # 간선의 양 끝점
    adj[s].append(e)
    adj[e].append(s)

res = 0
for i in range(1, n+1) :
    if visited[i] == False :
        DFS(i) # 최대한 인접한 정점들을 연결합니다.
        res += 1 # 연결 요소의 개수 + 1
        
print(res)
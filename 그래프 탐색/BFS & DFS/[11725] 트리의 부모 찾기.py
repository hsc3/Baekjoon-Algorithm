'''
[11725] 트리의 부모 찾기 | Silver 2 | 그래프
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
'''
# 재귀보단 반복문 사용이 빠르다.
# 큐를 사용할때 꼭 deque 사용.
import sys
from collections import deque
input = sys.stdin.readline
def BFS() : # 너비우선탐색
    q = deque([1])
    while q :
        node = q.popleft()
        for i in adj[node] :
            if not parent[i] :
                parent[i] = node
                q.append(i)
    
N = int(input())
adj = {}
parent = [0 for _ in range(N+1)]
parent[1] = 1
for i in range(N-1) :
    a, b = map(int, input().split())
    adj[a] = adj.get(a, []) + [b]
    adj[b] = adj.get(b, []) + [a]
BFS()
print(*parent[2:], sep='\n')
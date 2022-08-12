'''
[13116] 30번 | Silver 4 | 자료구조 (Tree)
완전이진트리에서 M(A,B)의 값을 구하여라.
M(A,B)는 1에서 A까지의 경로, 1에서 B까지의 경로 중 최대 조상노드를 구하여 10을 곱한 값이다.
'''
import sys ; 
input = sys.stdin.readline
def M(A, B) :
    while True :
        if A == B :
            return 10*A
        elif A > B :
            A //= 2
        else :
            B //= 2
    
T = int(input())
for _ in range(T) :
    A, B = map(int, input().split()) 
    a = []
    print(M(A, B))

'''
import sys
sys.setrecursionlimit(int(1e5))
input=sys.stdin.readline

def dfs(cur, d):
    check[cur]=True
    depth[cur]=d
    for nxt in graph[cur]:
        if not check[nxt]:
            parent[nxt]=cur
            dfs(nxt, d+1)

def lca(a,b):
    while depth[a]!=depth[b]:
        if depth[a]>depth[b]:
            a=parent[a]
        else:
            b=parent[b]
    while a!=b:
        a=parent[a]
        b=parent[b]
    return a

depth=[0]*1024
check=[False]*1024
parent=[0]*1024
graph=[[] for i in range(1024)]
for a in range(1,512):
    graph[a].append(2*a)
    graph[a].append(2*a+1)

dfs(1,0)

T=int(input())
for _ in range(T):
    A,B=map(int,input().split())
    print(lca(A,B)*10)
'''

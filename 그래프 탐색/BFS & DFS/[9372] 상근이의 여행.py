'''
[9372] 상근이의 여행 | Silver 4 | 그래프 (DFS)
상근이는 겨울방학을 맞아 N개국을 여행하면서 자아를 찾기로 마음먹었다. 
하지만 상근이는 새로운 비행기를 무서워하기 때문에, 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.
이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.
상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.
'''
import sys
input = sys.stdin.readline

def DFS() :
    cnt = 0 # 타는 비행기의 수
    stack = [1]
    while stack :
        p = stack.pop()
        for i in adj[p] :
            if not visited[i] : # 방문하지 않은 국가인 경우
                stack.append(i)
                visited[i] = True
                cnt += 1
    return cnt

T = int(input())
for _ in range(T) : 
    N, M = map(int, input().split())
    visited = [False for _ in range(N+1)]
    visited[1] = True
    adj = [[] for _ in range(N+1)]
    for _ in range(M) :
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    print(DFS())
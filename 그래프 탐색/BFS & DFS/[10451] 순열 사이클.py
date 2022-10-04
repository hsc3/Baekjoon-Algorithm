# [10451] 순열 사이클 | Silver 3 | https://www.acmicpc.net/problem/10451
import sys
input = sys.stdin.readline

"""def DFS(i, start):
    global cycle
    if visited[i]: # 이미 방문한 정점인 경우
        if i == start:
            cycle += 1
        return

    else: # 아직 방문하지 않은 점점인 경우
        visited[i] = True
        return DFS(arr[i], start)
        

answer = []
for _ in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False for _ in range(N)]
    cycle = 0
    for i in range(1, N+1):
        if not visited[i]:
            DFS(i, i)
    answer.append(cycle)

print(*answer, sep='\n')"""


answer = []
for _ in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False for _ in range(N)]
    cycle = 0
    for i in range(1, N+1):
        if not visited[i]:
            cycle += 1
            i = arr[i]
            while not visited[i]: # 사이클을 형성하는 모든 정점 방문
                visited[i] = True
                i = arr[i]
    answer.append(cycle)
    
print(*answer, sep='\n')
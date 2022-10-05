# [1926] 그림 | Silver 1 | https://www.acmicpc.net/problem/1926
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(i, j):
    queue = deque([[i, j]])
    length = 1 # 그림의 길이
    while queue:
        x, y = map(int, queue.popleft())
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < M and paper[xx][yy] == 1:
                paper[xx][yy] = 0
                length += 1
                queue.append([xx, yy])

    return length

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = [] # 그림의 길이들을 저장

for i in range(N):
    for j in range(M):
        if paper[i][j] == 1:
            paper[i][j] = 0
            answer.append(BFS(i, j))

print(len(answer))
print(max(answer) if answer else 0)
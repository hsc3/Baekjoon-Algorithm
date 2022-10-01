# [14502] 연구소 | Gold 4 | https://www.acmicpc.net/problem/14502
from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def makeWall(cnt):
    if cnt == 3:
        BFS()
        return

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                makeWall(cnt+1)
                matrix[i][j] = 0

def BFS():

    global answer
    copiedMatrix = deepcopy(matrix)
    queue = deque()
    for i in range(N):
        for j in range(M):
            if copiedMatrix[i][j] == 2:
                queue.append([i, j])

    while queue:
        x, y = map(int, queue.popleft())
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < M and copiedMatrix[xx][yy] == 0:
                copiedMatrix[xx][yy] = 2
                queue.append([xx, yy])

    cnt = 0
    for i in range(N):
        for j in range(M):
            if copiedMatrix[i][j] == 0:
                cnt += 1

    answer = max(answer, cnt)
    return

if __name__ == "__main__":

    answer = 0

    N, M = map(int, input().split())
    virus = deque()
    matrix = []

    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(len(arr)):
            if arr[j] == 2:
                virus.append([i, j])
        matrix.append(arr)

    makeWall(0)
    print(answer)
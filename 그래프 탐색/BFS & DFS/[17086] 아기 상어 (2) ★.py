# [17086] 아기 상어 (2) | Silver 2 | 그래프
'''
N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.
어떤 칸의 안전 거리는 "그 칸과 가장 거리가 가까운 아기 상어와의 거리"이다.
두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.
안전 거리가 가장 큰 칸을 구해보자.
'''
import sys
from collections import deque
input = sys.stdin.readline
# 이동 가능한 위치 (8방향)
dx = [1, 1, -1, -1, 0, 0, 1, -1]
dy = [1, -1, 1, -1, 1, -1, 0 ,0]

N, M = map(int, input().split())
arr = []
queue = deque()

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1: # 상어의 위치를 저장하고, 1 -> 0 변경 (이동 거리인 0으로)
            queue.append([i, j])
            row[j] = 0
        else:
            row[j] = float("inf") # 상어의 위치가 아니면, 무한히 큰 값 저장
    arr.append(row)

answer = 0
while queue:
    x, y = map(int, queue.popleft())
    answer = max(answer, arr[x][y])

    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < M and arr[xx][yy] > arr[x][y] + 1: # 아직 방문하지 않은 경우에만, 탐색 (방문한 경우, 이미 최소 거리가 저장되어 있다)
            arr[xx][yy] = arr[x][y] + 1
            queue.append([xx, yy])

print(answer)


# for i in range(N):
#     row = list(map(int, input().split()))
#     for j in range(len(row)):
#         if row[j] == 1: # 상어의 위치를 저장하고, 1 -> 0 변경 (이동 거리로 변경)
#             shark.append([i,j])
#             row[j] = 0
#         else:
#             row[j] = float("inf") # 상어가 없는 위치, 최소 이동 거리를 구하기 위해 큰 값으로 변경
#     arr.append(row)
#
# # 상어의 위치에서 주변 탐색을 시작
# for s in shark:
#     q = deque([s])
#     while q:
#         x, y = map(int, q.popleft())
#         for i in range(8):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0 <= xx < N and 0 <= yy < M and [xx, yy] not in shark and arr[xx][yy] > arr[x][y] + 1: # 최소 이동 거리인 경우, 갱신
#                 arr[xx][yy] = arr[x][y] + 1
#                 q.append([xx,yy])
#
# answer = 0
# for row in arr:
#     answer = max(answer, max(row))
# print(answer)
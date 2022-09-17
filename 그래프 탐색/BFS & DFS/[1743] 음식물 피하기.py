# [1743] 음식물 피하기 | Silver 1 | 그래프 탐색
'''
코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다.
이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다.
통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다.
선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.
'''
import sys
from collections import deque
input = sys.stdin.readline

move = [[1, 0], [-1, 0],[0, 1], [0, -1]]

def BFS(i, j):
    global answer

    queue = deque([[i, j]])
    cnt = 1 # 음식물의 크기
    graph[i][j] = 0 # 방문 표시

    while queue:
        x, y = map(int, queue.popleft())
        for dx, dy in move:
            xx, yy = x + dx, y + dy
            if 0 <= xx < N and 0 <= yy < M and graph[xx][yy] == 1: # 인접한 음식물 방문
                queue.append([xx, yy])
                graph[xx][yy] = 0
                cnt += 1

    answer = max(answer, cnt)

N, M, K = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    graph[i-1][j-1] = 1 # 음식물이 있는 좌표

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: # 음식물의 위치에서 너비우선탐색 시작
            BFS(i, j)

print(answer)


# import sys
# from collections import deque
# input = sys.stdin.readline
#
# move = [[1, 0], [-1, 0],[0, 1], [0, -1]]
# N, M, K = map(int, input().split())
# graph = [[0 for _ in range(M)] for _ in range(N)]
# for _ in range(K):
#     i, j = map(int, input().split())
#     graph[i-1][j-1] = 1
#
# answer = 0
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             queue = deque([[i, j]])
#             graph[i][j] = 0
#             cnt = 1 # 음식물의 크기
#
#             while queue:
#                 x, y = map(int, queue.popleft())
#
#                 for dx, dy in move:
#                     xx = x + dx
#                     yy = y + dy
#                     # 인접하고 방문하지 않은 음식물의 좌표 방문
#                     if 0 <= xx < N and 0 <= yy < M and graph[xx][yy] == 1:
#                         queue.append([xx, yy])
#                         cnt += 1
#                         graph[xx][yy] = 0
#
#             answer = max(answer, cnt)
#
# print(answer)
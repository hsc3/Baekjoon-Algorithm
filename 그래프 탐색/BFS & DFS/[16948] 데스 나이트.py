# [16948] 데스 나이트 | Silver 1 | 그래프 탐색
'''
게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다. 데스 나이트는 체스판 밖으로 벗어날 수 없다.
출력 : 첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

move = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
chess = [[float("inf") for _ in range(N)] for _ in range(N)]
chess[r1][c1] = 0

queue = deque([[r1, c1]])
while queue:
    x, y = map(int, queue.popleft())

    for dx, dy in move:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < N and 0 <= yy < N and chess[x][y] + 1 < chess[xx][yy]:
            chess[xx][yy] = chess[x][y] + 1
            queue.append([xx, yy])

print(chess[r2][c2] if chess[r2][c2] != float("inf") else -1)

# import sys
# from heapq import heappush, heappop
# input = sys.stdin.readline
#
# move = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
#
# N = int(input())
# r1, c1, r2, c2 = map(int, input().split())
# chess = [[float("inf") for _ in range(N)] for _ in range(N)] # 최소 이동 횟수 저장
# chess[r1][c1] = 0
#
#
# heap = []
# heappush(heap, [chess[r1][c1], r1, c1])
# while heap:
#     count, x, y = map(int, heappop(heap)) # 최단 경로의 이동 횟수와 해당 좌표
#
#     for dx, dy in move:
#         xx = x + dx
#         yy = y + dy
#         if 0 <= xx < N and 0 <= yy < N:
#             if count + 1 < chess[xx][yy]: # [x, y] 위치를 기준으로 최단 경로를 갱신할 수 있는 경우
#                 chess[xx][yy] = count + 1 # 최소 이동 횟수 갱신
#                 heappush(heap, [chess[xx][yy], xx, yy]) # 최소 힙에 [xx, yy]를 넣는다.
#
# print(chess[r2][c2] if chess[r2][c2] != float("inf") else -1)
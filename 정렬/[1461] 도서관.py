# [1461] 도서관 | Gold 5 | https://www.acmicpc.net/problem/1461

import sys
input = sys.stdin.readline

answer = 0
N, M = map(int, input().split())
books = sorted([0] + list(map(int, input().split()))) # [-39, -37, -29, -28, -6, 0, 2, 11]
zero_idx = books.index(0)

# 좌표 0 기준, 왼쪽과 오른쪽에 위치한 책들의 좌표를 저장한다.
west = [-book for book in books[:zero_idx+1]] # [39, 37, 29, 28, 6, 0]
east = books[zero_idx:][::-1] # [11, 2, 0]

w_i, e_i = 0, 0
if west[w_i] > east[e_i]: # 왼쪽과 오른쪽 중 더 먼 곳을 마지막에 이동한다. (돌아오지 않는다.)
    answer += west[w_i]
    w_i += M
else:
    answer += east[e_i]
    e_i += M

for i in range(w_i, len(west), M): # 나머지 책들의 위치까지 왕복 거리를 더한다.
    answer += (2 * west[i])
for i in range(e_i, len(east), M):
    answer += (2 * east[i])

print(answer)

'''
import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappush, heappop

answer = 0
N, M = map(int, input().split())
books = sorted(list(map(int, input().split()))) # [-39, -37, -29, -28, -6, 2, 11]
west, east = deque(), deque() # 좌표 0 기준, 왼쪽과 오른쪽에 위치한 책들의 좌표
for i in range(N):
    if books[i] < 0:
        west.append(-books[i]) # [39, 37, 29, 28, 6]
    else:
        east.appendleft(books[i]) # [11, 2]

data = [] # M개 기준으로 책을 분리하여 멀리 있는 좌표를 저장한다.
for i in range(0, len(west), M):
    heappush(data, -west[i]) # [-39, -29, -6]
for i in range(0, len(east), M):
    heappush(data, -east[i]) # [-39, -29, -11, -6]

answer = -1 * (heappop(data) + 2 * sum(data)) # 39 + 2 * (29 + 11 + 6)
print(answer)
'''
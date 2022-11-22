# [5014] 스타트링크 | Silver 1 | https://www.acmicpc.net/problem/5014
import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)] # 층별 엘리베이터를 탄 횟수
visited[S] = 1
queue = deque([S])
while queue:
    stair = queue.popleft()
    if stair == G:
        break

    if stair + U <= F and visited[stair + U] == 0: # 윗층 이동
        visited[stair + U] = visited[stair] + 1
        queue.append(stair + U)
    if stair - D >= 1 and visited[stair - D] == 0: # 아랫층 이동
        visited[stair - D] = visited[stair] + 1
        queue.append(stair - D)

print("use the stairs" if visited[G] == 0 else visited[G]-1)
'''
[7562] 나이트의 이동 | Silver 1 | 그래프 (BFS)
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
'''
import sys, collections
from collections import deque
input = sys.stdin.readline

# 나이트가 이동할 수 있는 모든 위치
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

# 너비우선탐색 BFS
def BFS():
    while q :
        x, y, cnt = map(int, q.popleft())
        if x == x2 and y == y2: # 목표 지점으로 이동하면 종료
            return cnt
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < l and 0 <= yy < l and not visited[xx][yy]:
                visited[xx][yy] = True
                q.append([xx,yy,cnt+1])
                
t = int(input())
for _ in range(t):
    l = int(input()) # 체스판의 길이
    visited = [[False for _ in range(l)] for _ in range(l)]
    x1, y1 = map(int, input().split()) # 출발지점
    x2, y2 = map(int, input().split()) # 도착지점
    q = deque([x1,y1,0])
    print(BFS())
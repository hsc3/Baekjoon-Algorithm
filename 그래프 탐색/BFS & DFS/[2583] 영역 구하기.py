# [2583] 영역 구하기 | Silver 1 | 그래프 (DFS, BFS)
'''
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.
M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split()) 
paper = [[0 for _ in range(N)] for _ in range(M)]

# --- 인접 행렬 생성
for _ in range(K) :
    y1, x1, y2, x2 = map(int, input().split()) 
    for i in range(x1, x2) :     
        for j in range(y1, y2) : 
            paper[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0] 

def bfs(i, j) :
    global paper, areaOfRectangle
    q = deque([[i, j]])
    paper[i][j] = 1
    cnt = 1

    while q :
        x, y = map(int, q.popleft())
                
        for k in range(4) :
            xx = x + dx[k]
            yy = y + dy[k]
            
            if (0 <= xx < M and 0 <= yy < N) and paper[xx][yy] == 0 :
                paper[xx][yy] = 1
                cnt += 1
                q.append([xx, yy])

    areaOfRectangle.append(cnt)

areaOfRectangle = []

for i in range(M) :
    for j in range(N) :
        if paper[i][j] == 0 :
            bfs(i, j)

print(len(areaOfRectangle))
print(*sorted(areaOfRectangle))

'''
# DFS -> stack

import sys
M, N, K = map(int, sys.stdin.readline().split())
g = [[0]*M for _ in range(N)]
for _ in range(K):
    frmx, frmy, tox, toy = map(int, sys.stdin.readline().split())

    for x in range(frmx, tox):
        for y in range(frmy, toy):
            g[x][y] = 1

land = []

def dfs(x,y):
    count = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    g[x][y] = 1
    stack = [(x,y)]

    while stack:
        x,y = stack.pop()
        for i in range(4):
            nxtx = x+dx[i]
            nxty = y+dy[i]

            if 0<=nxtx<N and 0<=nxty<M and g[nxtx][nxty] == 0:
                g[nxtx][nxty] = 1
                stack.append((nxtx, nxty))
                count += 1

    land.append(count)

for i in range(N):
    for j in range(M):
        if g[i][j] == 0:
            dfs(i,j)

land.sort()
print(len(land))
print(" ".join(str(x) for x in land))
'''
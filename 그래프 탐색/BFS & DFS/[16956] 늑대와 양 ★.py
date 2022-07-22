# [16956] 늑대와 양 / Silver 3 / 그래프
'''
크기가 R×C인 목장이 있고, 목장은 1×1 크기의 칸으로 나누어져 있다. 각각의 칸에는 비어있거나, 양 또는 늑대가 있다.
양은 이동하지 않고 위치를 지키고 있고, 늑대는 인접한 칸을 자유롭게 이동할 수 있다. 두 칸이 인접하다는 것은 두 칸이 변을 공유하는 경우이다.
목장에 울타리를 설치해 늑대가 양이 있는 칸으로 갈 수 없게 하려고 한다. 늑대는 울타리가 있는 칸으로는 이동할 수 없다. 울타리를 설치해보자.
'''
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

R, C = map(int, input().split())
wolfs = []  # 늑대의 위치
farm = [] # 목장
visited = [[False for _ in range(C)] for _ in range(R)] # 늑대의 방문 여부

for i in range(R):
    farm.append(list(input().rstrip()))
    for j in range(C):
        if farm[i][j] == 'W':
            wolfs.append([i, j])  # 늑대의 위치를 저장한다.
            visited[i][j] = True

# 너비우선탐색(queue) : 늑대의 위치에서 경로를 탐색하다가 양과 마주치면 이전 칸에 울타리를 설치한다.
protectable = 1  # 늑대를 양으로부터 막을 수 있는지 여부
for wolf in wolfs: # 각 늑대의 위치에서 탐색을 시작
    queue = deque([wolf])

    while queue:
        x, y = map(int, queue.popleft())

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            # 늑대가 이동할 수 있는 위치인지 확인 (farm 범위 안 O, 방문 X, 울타리 X)
            if 0 <= xx < R and 0 <= yy < C and not visited[xx][yy] and farm[xx][yy] != 'D':
                if farm[xx][yy] == 'S':  # 늑대가 양을 만난 경우 -> 이전 칸에 울타리를 세워야 한다.
                    if farm[x][y] == 'W':  # 이전 칸에 늑대가 위치한 경우이면 울타리를 세울 수 없다.
                        protectable = 0
                        break
                    else:  # 이전 칸에 울타리 설치
                        farm[x][y] = 'D'

                else: # 이동 가능한 위치로 저장
                    queue.append([xx, yy])
                    visited[xx][yy] = True

print(protectable)
if protectable:
    for row in farm:
        print(''.join(row))

# 울타리의 최소 개수를 구하는 문제 X -> 양과 늑대를 제외한 모든 곳에 울타리를 설치
'''
import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
map=[]
loc=[]
for i in range(n):
    s=input().rstrip().replace(".","D")
    for j in range(m):
        if s[j]=="W":
            loc.append((i,j))
    map.append(s)
    
dir=[(0,1),(0,-1),(1,0),(-1,0)]
ans=1
for x,y in loc:
    for dx,dy in dir:
        nx=x+dx
        ny=y+dy
        if 0<=nx<n and 0<=ny<m and map[nx][ny]=="S":
            ans=0
            break
    if ans==0:
        break
print(ans)
if ans!=0:
    for i in range(n):
        print(map[i])
'''

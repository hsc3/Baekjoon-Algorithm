# [7569] 토마토 | Gold 5 | 그래프 (BFS)
'''
토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다. 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''
import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1,  0,  0,  0,  0]
dy = [0,  0, -1,  1,  0,  0]
dz = [0,  0,  0,  0,  1, -1]

def BFS() :
    while queue :
        z, x, y = map(int, queue.popleft())
        for i in range(6) :
            zz = z + dz[i]
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=zz<H and 0<=xx<N and 0<=yy<M and tomato[zz][xx][yy] == 0 : # 익지 않은 토마토일 경우
                tomato[zz][xx][yy] = tomato[z][x][y] + 1 # 토마토가 익는데 걸린 날을 업데이트 합니다.
                queue.append([zz,xx,yy])
        
        
M, N, H = map(int, input().split()) # 가로, 세로, 높이
tomato = [] # tomato[h][n][m]
queue = deque([])
for h in range(H) :
    temp = []
    for n in range(N) :
        temp.append(list(map(int, input().split())))
        for m in range(M) :
            if temp[n][m] == 1 :
                queue.append([h,n,m])
    tomato.append(temp) # 모든 토마토의 위치 저장

BFS() # 너비우선탐색 -> 큐
res = 0
for i in tomato :
    for j in i :
        for k in j :
            if k == 0 :
                print(-1)
                exit(0)
        res = max(res, max(j))

print(res-1)
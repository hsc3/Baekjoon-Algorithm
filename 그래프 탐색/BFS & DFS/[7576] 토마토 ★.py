'''
[7576] 토마토 | Gold 5 | 그래프 (BFS)
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
(익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.)
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
'''
import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

m, n = map(int, input().split()) # 가로길이, 세로길이
tomato = [[0 for _ in range(m)] for _ in range(n)]
q = deque() # 모든 토마토의 위치를 저장

for i in range(n) :
    tomato[i] = list(map(int, input().split()))
    for j in range(m) :
        if tomato[i][j] == 1 :
            q.append([i,j]) # (큐에서 차례대로 꺼내어 차례대로 익어가는 것을 체크할 수 있음)

def BFS() :
    while q :
        #print(*tomato, sep = '\n')
        #print("============================")
        x, y = map(int, q.popleft())
        for k in range(4) :
            xx = x + dx[k]
            yy = y + dy[k]
            # 아직 익지 않은 곳만 접근한다. 0이 아닌 곳은 더 빠른 시간 내에 익은 것. 체크할 필요 X
            if 0 <= xx < n and 0 <= yy < m and tomato[xx][yy] == 0 :
                    tomato[xx][yy] = tomato[x][y] + 1
                    q.append([xx, yy])
BFS()

res = 0
for t in tomato :
    if 0 in t : res = 0 ; break
    else : res = max(res, max(t))
print(res-1)
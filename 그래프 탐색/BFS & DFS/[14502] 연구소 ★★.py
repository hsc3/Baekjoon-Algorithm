'''
[14502] 연구소 | Gold 4 | 그래프(BFS), 구현
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.  
연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오
(0: 빈 공간, 1: 벽, 2: 바이러스)
'''
import sys, collections
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

# 바이러스가 퍼지는 시뮬레이터 함수, BFS
def Simulator() :
    global lab, virus, answer
    lab_test = deepcopy(lab)
    virus_test = deepcopy(virus)
    while virus_test : # 모든 바이러스 지점을 동시에 돌릴 수 있음 !!!!!!!!!!
        x, y = virus_test.popleft()
        for k in range(4) :
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < m and lab_test[xx][yy] == 0 :
                lab_test[xx][yy] = 2
                virus_test.append([xx,yy])
    safe = 0
    for l in lab_test :
        safe += l.count(0)
    answer = max(answer, safe)

# 벽 세우는 함수, BFS, 백트랙킹
def Barrier(cnt) :
    if cnt == 0 : # 모든 벽을 세운 경우, 바이러스 시뮬레이션을 돌린다. 
        Simulator()
        return

    for i in range(n) :
        for j in range(m) :
            if lab[i][j] == 0 : 
                lab[i][j] = 1 # 벽을 세우고 또다른 벽을 세우러 간다
                Barrier(cnt-1) # <-- lab[i][j]에 벽이 세워진 상태로 진행
                lab[i][j] = 0 # <-- 벽을 세우지 않은 상태로 진행 (백트랙킹)

# ------------------------------------------
# 변수 선언 및 할당
dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] # 이동 빙향
n, m = map(int, input().split()) # 연구소의 크기 
lab = [[] for _ in range(n)]
virus = deque() # 바이러스 위치를 저장하는 리스트
res = []

for i in range(n) :
        lab[i] = list(map(int, input().split()))
        for j in range(m) :
            if lab[i][j] == 2 : 
                virus.append([i,j])
# -------------------------------------------
# 벽 세우기
answer = 0
Barrier(3)
print(answer)
'''
def bfs():
    #2의 위치 필요
    que=deque()
    for i in range(len(pos2)):
        que.append([pos2[i][0],pos2[i][1]])
    visited=[[False]*m for _ in range(n)]
    v=0
    while que:
        x,y=que.popleft()
        visited[x][y]=True
        v+=1
        for i in move:
            nx=x+i[0]
            ny=y+i[1]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]==0:
                que.append([nx,ny])
                visited[nx][ny]=True
            
    return v

def dfs(px,py,cnt):
    global maxv
    if cnt==3:
        value=bfs()
        res=n*m-value-pos1_num-3
        if maxv<res:
            maxv=res
        return

    for i in range(px,n):
        for j in range(py if i==px else 0,m):
            if graph[i][j]!=0:
                continue
            graph[i][j]=1
            dfs(i,j,cnt+1)
            graph[i][j]=0
                

n,m=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(n)]

pos2=[]
pos1_num=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            pos2.append([i,j])
        if graph[i][j]==1:
            pos1_num+=1

move=[(1,0),(-1,0),(0,1),(0,-1)]
maxv=0


dfs(0,0,0)

print(maxv)
'''
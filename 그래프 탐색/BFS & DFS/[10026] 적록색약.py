'''
[10026] 적록색약 | Gold 5 | 그래프 (BFS)
적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
(적록색약인 사람은 빨간색과 초록색을 구분하지 못한다.)
'''
import sys
from collections import deque
input = sys.stdin.readline
# ------------------------------------------------------------------------------------
dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1]
n = int(input())
color = [[] for _ in range(n)]
for i in range(n) :
    color[i] = list(input().rstrip())
# ------------------------------------------------------------------------------------
def BFS(i, j) : 
    q = deque()
    q.append([i, j])
    while q :
        x, y = map(int, q.popleft())
        # visited[x][y] = True -> 여기서 접근하는 것보다
        for k in range(4) :
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == False and color[x][y] == color[xx][yy] :
                q.append([xx,yy])
                visited[xx][yy] = True # 여기서 바로 접근을 해야 시간단축할 수 있음
# ------------------------------------------------------------------------------------
# 적록색맹이 아닌 경우
visited = [[False for _ in range(n)] for _ in range(n)]
no_count = 0 
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False :
            BFS(i,j)
            no_count += 1 # 구분할 수 있는 색의 수 1 증가
# -------------------------------------------------------------------------------------
# 적록색맹인 경우 - 적색과 녹색 통일
for i in range(n) :
    for j in range(n) :
        if color[i][j] == "R" :
            color[i][j] = "G"
visited = [[False for _ in range(n)] for _ in range(n)]
count = 0
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False :
            BFS(i,j)
            count += 1

print(no_count, count)
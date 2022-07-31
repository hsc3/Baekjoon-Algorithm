'''
[4963] 섬의 개수 | Silver 2 | 그래프 (DFS)
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(x, y) :
    a[x][y] = 0
    for i in range(8) :
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < m and 0 <= yy < n and  a[xx][yy] == 1 :
            DFS(xx, yy)

dx = [-1,0,1,1,1,0,-1,-1]
dy = [-1,-1,-1,0,1,1,1,0]
res = []

while True : # 여러 개의 테스트 케이스
    cnt = 0
    n, m = map(int, input().split())
    if n == m == 0 : break

    a = [list(map(int, input().split())) for _ in range(m)]
    for i in range(m) :
        for j in range(n) :
            if a[i][j] == 1 : # 섬 지점에서 DFS 수행
                DFS(i, j)
                cnt += 1

    res.append(cnt)

print(*res, sep = '\n')
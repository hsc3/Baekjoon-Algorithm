'''
[2468] 안전 영역 | Silver 1 | 그래프 (DFS)
어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오. 
'''
import sys
input = sys.stdin.readline

m = []
n = int(input())
s = 100 # 가장 적은 비의 양
l = 1 # 가장 많은 비의 양

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def DFS(x, y) :
    visited[x][y] = True
    for i in range(4) : 
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and visited[xx][yy] == False and m[xx][yy] > rain : # 물에 잠기지 않은 땅인 경우
            DFS(xx, yy)

for _ in range(n) :
    temp = list(map(int, input().split()))
    s = min(s, min(temp))
    l = max(l, max(temp)) # => max_height = max(map(max, m))
    m.append(temp) # 땅의 높이 정보

res = []
# 비의 양보다 땅이 높으면 1, 아니면 0 -> 1만 방문한다.
for rain in range(s, l+1) :
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if m[i][j] > rain and visited[i][j] == False : 
                DFS(i,j)
                cnt += 1 # 잠기지 않은 영역의 개수 1 증가
    res.append(cnt)
print(max(res))
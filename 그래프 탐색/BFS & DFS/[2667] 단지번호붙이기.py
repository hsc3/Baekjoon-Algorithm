'''
[2667] 단지번호붙이기 | Silver 1 | 그래프 (DFS)
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
(연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.)
'''

def DFS(x, y) :
    global cnt
    cnt += 1
    a[x][y] = 0 # 방문
    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and a[xx][yy] == 1 : # 아직 방문하지 않은 지점으로 이동
            DFS(xx, yy)


if __name__ == "__main__" :
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    res = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for x in range(n) :
        for y in range(n) :
            if a[x][y] == 1 :
                cnt = 0
                DFS(x, y)
                res.append(cnt)
    print(len(res))
    res.sort()
    print(*res, sep = '\n')

'''
import sys
input = sys.stdin.readline
N = int(input())
home = []
visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N) :
    home.append(input())

ans = []
for x in range(N) :
    for y in range(N) :
        if visited[x][y] == False and home[x][y] == '1' :
            stack = []
            cnt = 0
            stack.append([x,y])
            while stack : 
                axis = stack.pop()
                i = axis[0]
                j = axis[1]
                if visited[i][j] == False :
                    cnt += 1
                    visited[i][j] = True
                
                if j-1 >= 0 and visited[i][j-1] == False and home[i][j-1] == '1' : # 왼쪽
                    stack.append([i,j-1]) 
                    
                if i+1 < N and visited[i+1][j] == False and home[i+1][j] == '1' : # 아래쪽
                    stack.append([i+1,j]) 
                    
                if j+1 < N and visited[i][j+1] == False and home[i][j+1] == '1' : # 오른쪽
                    stack.append([i,j+1]) 
                    
                if i-1 >= 0 and visited[i-1][j] == False and home[i-1][j] == '1': # 위쪽
                    stack.append([i-1,j]) 
            ans.append(cnt)
                    
print(len(ans))
ans.sort()
print(*ans, sep = '\n')
'''
'''
[1388] 바닥 장식 / Silver 3 / 그래프 탐색 (DFS, BFS)
이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 
두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.
기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
floor = [list(input().rstrip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

move = {'-' : [[0,1], [0,-1]], '|' : [[1,0], [-1,0]]} # 타일 모양에 따른 탐색 방향
res = 0 # 타일의 갯수

# 너비우선탐색 (BFS) -> Queue
for i in range(N) :
    for j in range(M) :
        if not visited[i][j] :
            tile = floor[i][j] # 타일의 모양
            visited[i][j] = True
            queue = [[i,j]]
            res += 1
            
            while queue :
                x, y = map(int, queue.pop(0))

                for k in range(2) :
                    xx, yy = x + move[tile][k][0], y + move[tile][k][1]
                    if 0 <= xx < N and 0 <= yy < M and floor[xx][yy] == tile and not visited[xx][yy] :
                        visited[xx][yy] = True
                        queue.append([xx, yy])
            
print(res)
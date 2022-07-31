'''
[2178] 미로탐색 | Silver 1 | 그래프 (BFS)
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
cost = [[float("inf") for _ in range(m)] for _ in range(n)]
cost[0][0] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = [[0,0]]
while q :
    #for column in cost :
    #    print(*column, sep=' ')
    #print("-----------------------")
    x, y = map(int, q.pop(0))
    if maze[x][y] == 1 : # 구역을 확인했음을 표시
        maze[x][y] = 0
    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]
        # 아직 확인하지 않았고, 기존 비용보다 새로운 비용이 적을 경우. (새로운 비용이 높을 경우, 탐색할 필요 없음)
        if 0 <= xx < n and 0 <= yy < m and maze[xx][yy] == 1 and cost[xx][yy] > cost[x][y] + 1 :
            q.append([xx, yy])
            cost[xx][yy] = cost[x][y] + 1

print(cost[n-1][m-1])
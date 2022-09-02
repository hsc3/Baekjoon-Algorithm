# [3184] 양 | Silver 1 | 그래프 탐색 (BFS)
'''
마당은 행과 열로 이루어진 직사각형 모양이다. 글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다.
한 칸에서 수평, 수직만으로 이동하며 울타리를 지나지 않고 다른 칸으로 이동할 수 있다면, 두 칸은 같은 영역 안에 속해 있다고 한다. 마당에서 "탈출"할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주한다.
다행히 우리의 양은 늑대에게 싸움을 걸 수 있고 영역 안의 양의 수가 늑대의 수보다 많다면 이기고, 늑대를 우리에서 쫓아낸다. 그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다.
맨 처음 모든 양과 늑대는 마당 안 영역에 존재한다. 아침이 도달했을 때 살아남은 양과 늑대의 수를 출력하는 프로그램을 작성하라.
'''
import sys
from collections import deque
input = sys.stdin.readline

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
N, M = map(int, input().split())
field = [list(input().rstrip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

answer = [0, 0] # 살아남은 양과 늑대의 수

for i in range(N):
    for j in range(M):
        # 아직 방문하지 않았고, 울타리가 아닌 경우 -> 해당 영역의 탐색을 시작한다.
        if not visited[i][j] and field[i][j] != '#':
            queue = deque([[i, j]])
            visited[i][j] = True
            sheep, wolf = 0, 0 # 영역 안의 양, 늑대의 수

            while queue:
                x, y = map(int, queue.popleft())
                # 방문한 영역에 늑대 혹은 양이 있는 경우, 해당 영역 안의 늑대 혹은 양의 수를 누적한다.
                if field[x][y] == 'o':
                    sheep += 1
                elif field[x][y] == 'v':
                    wolf += 1

                for dx, dy in move:
                    xx, yy = x + dx, y + dy
                    # field[xx][yy]로 이동할 수 있는 경우 (같은 울타리 안의 영역이고, 아직 방문하지 않은 경우)
                    if 0 <= xx < N and 0 <= yy < M and not visited[xx][yy] and field[xx][yy] != '#':
                        visited[xx][yy] = True
                        queue.append([xx, yy])

            # 해당 영역 안에서 살아남은 양, 늑대의 수를 전체 값에 누적한다.
            if sheep > wolf:
                answer[0] += sheep
            else:
                answer[1] += wolf

print(*answer)
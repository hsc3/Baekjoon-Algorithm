# [14502] 연구소 | Gold 4 | https://www.acmicpc.net/problem/14502
# 벽을 세우고 (백트랙킹) 바이러스 시뮬레이션을 돌린다(너비 우선 탐색)
from copy import deepcopy
import sys; input = sys.stdin.readline
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def checkLab(my_lab):
    clean_area = 0
    for i in range(N):
        clean_area += my_lab[i].count(0)
    return clean_area

def BFS(lab):
    my_virus = deepcopy(virus)
    my_lab = deepcopy(lab)

    while my_virus:
        x, y = map(int, my_virus.pop(0))
        for i in range(4):
            xx, yy = x + move[i][0], y + move[i][1]
            if 0 <= xx < N and 0 <= yy < M and my_lab[xx][yy] == 0:
                my_lab[xx][yy] = 2
                my_virus.append([xx, yy])

    return checkLab(my_lab)


def makeWall(cnt, i, empty, lab):
    global answer
    if cnt == 3:
        answer = max(answer, BFS(lab))
        return

    for i in range(i, len(empty)):
        x, y = map(int, empty[i])
        lab[x][y] = 1
        makeWall(cnt+1, i+1, empty, lab)
        lab[x][y] = 0

if __name__ == "__main__":
    answer = 0
    N, M = map(int, input().split())
    lab = []
    virus = []
    empty = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if row[j] == 2:
                virus.append([i, j])
            elif row[j] == 0:
                empty.append([i, j])
        lab.append(row)

    makeWall(0, 0, empty, lab)
    print(answer)
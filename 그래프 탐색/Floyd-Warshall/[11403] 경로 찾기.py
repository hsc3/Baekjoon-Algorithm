'''
[11403] 경로 찾기  | Silver 1 | 그래프 (Floyd-Warshall)
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k] and matrix[k][j]: # i -> k -> j 를 거치는 경로가 있는 경우, i -> j 로 갈 수 있다.
                matrix[i][j] = 1

for r in matrix:
    print(*r)

'''
import sys
input = sys.stdin.readline
N = int(input())
matrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N) :
    matrix[i] = list(map(int, input().split()))
    for j in range(N) :
        if matrix[i][j] == 0 :
            matrix[i][j] = float("inf")

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for i in range(N) :
    for j in range(N) :
        if matrix[i][j] == float("inf") : matrix[i][j] = 0 
        else : matrix[i][j] = 1 
        print(matrix[i][j], end = ' ')
    print()
'''
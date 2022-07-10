'''
[11660] 구간 합 구하기 (5) / Silver 1 / 다이나믹 프로그래밍
N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

answer = []
N, M = map(int, input().split())

# 2차원 배열의 숫자들을 입력받고, 누적 합을 계산한다.
matrix = [[0]*(N+1)]
for _ in range(N):
    matrix.append([0] + list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        matrix[i][j] += (matrix[i][j-1] + matrix[i-1][j] - matrix[i-1][j-1])

# (x1, y1)부터 (x2, y2) 구간의 합을 구한다.
for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    answer.append(matrix[x2][y2] - (matrix[x2][y1-1] + matrix[x1-1][y2] - matrix[x1-1][y1-1]))

print(*answer, sep='\n')
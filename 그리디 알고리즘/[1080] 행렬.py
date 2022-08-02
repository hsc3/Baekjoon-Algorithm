# [1080] 행렬 | Silver 1 | 그리디 알고리즘
'''
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.
행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)
'''
import sys
input = sys.stdin.readline

def reverse(i, j): # 3x3의 행렬을 뒤집는다.
    for row in range(i, i+3):
        for col in range(j, j+3):
            A[row][col] = 1 - A[row][col]

N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]

answer = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]: # 원소를 뒤집어야 하는 경우
            reverse(i, j)
            answer += 1

print(answer if A == B else -1)
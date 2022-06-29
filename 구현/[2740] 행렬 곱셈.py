'''
[2740] 행렬 곱셈 / Silver 5 / 구현
N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

# B 행렬의 X와 Y축을 변경한다.
B = list(zip(*B))

res = []
for i in range(N) :
    row = []
    for j in range(K) :
        tmp = []
        for x, y in zip(A[i], B[j]) :
            tmp.append(x*y)
        row.append(sum(tmp))

    res.append(row)

for row in res :
    print(*row, sep=' ')

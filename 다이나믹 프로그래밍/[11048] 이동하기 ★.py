'''
[11048] 이동하기 | Silver 1 | Dynamic Programming
준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.
'''
import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split()) # 방의 x, y 좌표
candy = [list(map(int, input().split())) for _ in range(N)] # 방에 놓인 사탕 수 입력
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for x in range(1, N+1) :
    for y in range(1, M+1) :
        dp[x][y] = candy[x-1][y-1] + max(dp[x-1][y], dp[x][y-1], dp[x-1][y-1])

print(dp[N][M])
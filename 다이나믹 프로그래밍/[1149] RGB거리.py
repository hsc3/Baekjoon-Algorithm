# [1149] RGB거리
# Silver 1 >> 다이나믹 프로그래밍
import sys 
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N) :
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))

'''
import sys 
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N) :
    for j in range(3) :
        minVal = float("inf")
        for k in range(3) :
            if j != k and dp[i-1][k] < minVal :
                minVal = dp[i-1][k]
        dp[i][j] += minVal

print(min(dp[N-1]))
'''
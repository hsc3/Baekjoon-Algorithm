# [1463] 1로 만들기
# Silver 3 >> 다이나믹 프로그래밍
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0 and dp[i // 3] + 1 < dp[i] :
        dp[i] = dp[i // 3] + 1
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i] :
        dp[i] = dp[i // 2] + 1
    
print(dp[N])

'''
N = int(input())
dp = [0] * (N+1)

for i in range(N, 1, -1) :
    if i % 3 == 0 :
        if dp[i // 3] == 0 : 
            dp[i // 3] = dp[i] + 1
        elif dp[i] + 1 < dp[i // 3] :
            dp[i // 3] = dp[i] + 1
    
    if i % 2 == 0: 
        if dp[i // 2] == 0 :
            dp[i // 2] = dp[i] + 1
        elif dp[i] + 1 < dp[i // 2] :
            dp[i // 2] = dp[i] + 1

    if dp[i-1] == 0 :
        dp[i-1] = dp[i] + 1
    elif dp[i] + 1 < dp[i - 1]:
        dp[i - 1] = dp[i] + 1

print(dp[1])
'''
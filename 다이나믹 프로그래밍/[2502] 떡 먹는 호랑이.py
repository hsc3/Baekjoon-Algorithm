# [2502] 떡 먹는 호랑이 | Silver 2 | https://www.acmicpc.net/problem/2502
import sys
input = sys.stdin.readline

D, K = map(int, input().split())
dp = [0] * (D+1)
dp[D] = K

for prev in range(K // 2 + 1, K): # 마지막의 전날에 준 떡의 개수
    dp[D-1] = prev
    for i in range(D, 2, -1):
        if dp[i] >= 2 * dp[i-1]: # 성립 불가 (다음날에 더 적은 떡을 준 경우)
            break
        else:
            dp[i-2] = dp[i] - dp[i-1]
    if dp[1] != 0: # 성립한 경우
        break

print(dp[1])
print(dp[2])
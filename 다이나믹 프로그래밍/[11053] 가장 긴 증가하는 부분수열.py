# [11053] 가장 긴 증가하는 부분수열 | https://www.acmicpc.net/problem/11053
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * 1001
for num in arr :
    if dp[num] == 0 :
        dp[num] = max(dp[:num]) + 1
    else :
        dp[num] = max(dp[num], max(dp[:num]) + 1)
print(max(dp))
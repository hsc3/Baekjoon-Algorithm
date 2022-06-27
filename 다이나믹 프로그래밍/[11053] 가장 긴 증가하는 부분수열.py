'''
[11053] 가장 긴 증가하는 부분수열 / Silver 2 / 다이나믹 프로그래밍
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split())) # [10 20 10 30 20 50]

dp = [0] * 1001

for num in arr :
    if dp[num] == 0 :
        dp[num] = max(dp[:num]) + 1
    else :
        dp[num] = max(dp[num], max(dp[:num]) + 1)
        
print(max(dp))

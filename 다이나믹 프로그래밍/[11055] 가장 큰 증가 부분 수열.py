# [11055] 가장 큰 증가 부분 수열 | Silver 2 | Dynamic Programming
# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.insert(0, 0)

dp = [0] * (N+1)

for i in range(1, N+1) :
    for j in range(i-1,-1,-1) :
        
        # if 조건절에 최대한 많은 조건을 담아서, 실행 횟수를 줄인다.
        if numbers[i] > numbers[j] and dp[j] + numbers[i] > dp[i] :
            dp[i] = dp[j] + numbers[i]

print(max(dp))
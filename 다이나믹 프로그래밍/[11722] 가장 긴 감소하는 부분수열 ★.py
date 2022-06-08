# [11722] 가장 긴 감소하는 부분수열 | https://www.acmicpc.net/problem/11722
N = int(input())
arr = list(map(int, input().split()))
dp = [1 for idx in range(N)]

for i in range(1, N) :
    for j in range(0, i) :
        if arr[j] > arr[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

'''
n = int(input())
num = list(map(int, input().split()))
dp = [0] * 1002 <<-- 모든 숫자에 대해 값을 저장. 비교가 편한 장점이 있음.
for i in num: <<-- for문이 하나로 줄어듬. 시간복잡도 감소
    if dp[i]:
        dp[i] = max(dp[i], max(dp[i + 1:]) + 1)
        continue
    dp[i] += max(dp[i + 1:]) + 1
print(max(dp))
'''
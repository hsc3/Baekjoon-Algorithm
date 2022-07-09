'''
[11722] 가장 긴 감소하는 부분수열 / Silver 2 / 다이나믹 프로그래밍
수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.
'''

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

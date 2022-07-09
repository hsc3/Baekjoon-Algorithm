'''
[11052] 카드 구매하기 / Silver 1 / 다이나믹 프로그래밍
N개의 카드를 구매하기 위한 최대금액을 구하는 프로그램을 작성하라.

<입력값> N : 구매하려고 하는 카드 수 (1 <= N <= 1000)
P[i] : 카드 i개가 들어있는 카드팩의 가격 (1 <= i <= N)
'''

N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
dp = [0 for _ in range(N+1)]
for n in range(1, N+1) :
    for i in range(0, n) :
        dp[n] = max(dp[i] + P[n-i], dp[n])

print(dp[N])

'''
N = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]


for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])
'''

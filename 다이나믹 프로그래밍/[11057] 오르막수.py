'''
[11057] 오르막수 / Silver 1 / 다이나믹 프로그래밍
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.
수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.
'''

N = int(input())
dp = [[1 for _ in range(10)] for _ in range(N)]

for i in range(1, N) :
    for j in range(10) :
        dp[i][j] = sum(dp[i-1][j:]) % 10007

print(sum(dp[N-1]) % 10007)

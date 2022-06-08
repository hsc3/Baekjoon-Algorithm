'''
[2225] 합분해 | https://www.acmicpc.net/problem/2225
0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''
# 경우의 수를 누적해나간다.
N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0] = 1
for i in range(N+1) : # 가치
    for j in range(1, K+1) : # 카드 수 (1개일 때부터 고려)
        for p in range(i+1) :
            dp[i][j] += dp[i-p][j-1] % 1000000000
print(dp[N][K] % 1000000000)

'''
n , k=map(int,input().split())
dp = [[0] * (n+1) for _ in range(k+1)]
dp[1]= [1] * (n+1)

for i in range(2, k+1): # 카드의 수
    for j in range(n+1): # 가치
        if j == 0:
            dp[i][j]=1
            continue

        dp[i][j] = dp[i-1][j] % 1000000000 + dp[i][j-1] % 1000000000

print(dp[k][n] % 1000000000)
'''
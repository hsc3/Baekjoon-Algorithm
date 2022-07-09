'''
[11727] 2xN 타일링(2) / Silver 3 / 다이나믹 프로그래밍
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
'''

N = int(input())
dp = [0 for _ in range(N)]
dp[0] = 1 
dp[1] = 3

for i in range(2,N) :
    dp[i] = dp[i-1] + 2 * dp[i-2] 

print(dp[N-1])

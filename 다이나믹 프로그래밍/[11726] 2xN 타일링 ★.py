'''
[11726] 2xN 타일링 / Silver 3 / 다이나믹 프로그래밍
2x1 타일과 2x2 타일을 이용해서 만들 수 있는 2xN 타일의 방법의 수
'''

# 피보나치 수열로 풀이가능 (수학적 방법)
n = int(input())
num_of_2x1 = n + 1        # 사용가능한 2x1 타일의 최대 개수 + 1 
num_of_1x2 = (n // 2) + 1 # 사용가능한 1x2 타일의 최대 개수 + 1 (1x2 타일은 무조건 2개를 세트로 사용해야한다)

# dp는 타일의 정렬 가능한 방법의 수를 저장 (ex) dp[2][2]는 aabb의 정렬 가능한 방법의 수 -> aabb, abab, baab, abba, baba, bbaa
dp = [[0 for j in range(0, num_of_1x2)] for i in range(0, num_of_2x1)]

for i in range(1, num_of_2x1) :
    dp[i][0] = 1 
for j in range(1, num_of_1x2) :
    dp[0][j] = 1

for i in range(1, num_of_2x1) :
    for j in range(1, num_of_1x2) :
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

ans = 0
for j in range(num_of_1x2) :
    i = n - (2 * j)
    ans += dp[i][j]
    
print(ans % 10007)

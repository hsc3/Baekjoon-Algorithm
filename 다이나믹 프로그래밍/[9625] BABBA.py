# 초기 화면 문자는 "A"
# 버튼을 누르면 B -> BA , A -> B로 바뀐다
# Q : 버튼을 K번 눌렀을 때, 화면에 출력되는 A와 B의 갯수

K = int(input())
dp = [[0,0] for _ in range(K+1)]
dp[0] = [1,0]
for k in range(1, K + 1) :
    dp[k][1] = dp[k-1][0] + dp[k-1][1]
    dp[k][0] = dp[k-1][1]
print(dp[k][0], dp[k][1])
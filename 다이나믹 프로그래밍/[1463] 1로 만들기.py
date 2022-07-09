'''
[1463] 1로 만들기 / Silver 3 / 다이나믹 프로그래밍
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
- X가 3으로 나누어 떨어지면, 3으로 나눈다.
- X가 2로 나누어 떨어지면, 2로 나눈다.
- 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0 and dp[i // 3] + 1 < dp[i] :
        dp[i] = dp[i // 3] + 1
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i] :
        dp[i] = dp[i // 2] + 1
    
print(dp[N])

'''
N = int(input())
dp = [0] * (N+1)

for i in range(N, 1, -1) :
    if i % 3 == 0 :
        if dp[i // 3] == 0 : 
            dp[i // 3] = dp[i] + 1
        elif dp[i] + 1 < dp[i // 3] :
            dp[i // 3] = dp[i] + 1
    
    if i % 2 == 0: 
        if dp[i // 2] == 0 :
            dp[i // 2] = dp[i] + 1
        elif dp[i] + 1 < dp[i // 2] :
            dp[i // 2] = dp[i] + 1

    if dp[i-1] == 0 :
        dp[i-1] = dp[i] + 1
    elif dp[i] + 1 < dp[i - 1]:
        dp[i - 1] = dp[i] + 1

print(dp[1])
'''

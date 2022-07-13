'''
[12852] 1로 만들기 (2) / Silver 1 / 다이나믹 프로그래밍
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 정답이 여러 가지인 경우에는 아무거나 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [float("inf") for _ in range(N+1)]
dp[1] = 0
prev = [0 for _ in range(N+1)]

for i in range(1, N):
    if i*3 <= N and dp[i] + 1 < dp[i*3]:
        dp[i*3] = dp[i] + 1
        prev[i*3] = i
    if i*2 <= N and dp[i] + 1 < dp[i*2]:
        dp[i*2] = dp[i] + 1
        prev[i*2] = i
    if dp[i] + 1 < dp[i+1]:
        dp[i+1] = dp[i] + 1
        prev[i+1] = i

answer = []
cursor = N
while True:
    answer.append(cursor)
    if cursor == 1:
        break
    cursor = prev[cursor]


print(len(answer)-1)
print(*answer)


# N = int(input())
# dp = [[N-i, 0] for i in range(N+1)] # dp -> [연산의 횟수, 연산 이전의 값]
#
# for i in range(N, 0, -1):
#     if i % 3 == 0 and dp[i][0]+1 <= dp[i//3][0]:
#         dp[i//3] = [dp[i][0] + 1, i]
#     if i % 2 == 0 and dp[i][0] + 1 <= dp[i//2][0]:
#         dp[i//2] = [dp[i][0] + 1, i]
#     if dp[i][0] + 1 <= dp[i-1][0]:
#         dp[i-1] = [dp[i][0] + 1, i]
#
# answer = deque()
# cursor = 1
# while True:
#     answer.appendleft(cursor)
#     if cursor == N:
#         break
#     cursor = dp[cursor][1]
#
#
# print(len(answer)-1)
# print(*answer)

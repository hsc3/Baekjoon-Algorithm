'''
[9184] 신나는 함수 실행 / Silver 2 / 다이나믹 프로그래밍
다음과 같은 재귀함수 w(a, b, c)가 있다.

if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns: 1
if a > 20 or b > 20 or c > 20, then w(a, b, c) returns: w(20, 20, 20)
if a < b and b < c, then w(a, b, c) returns: w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
otherwise it returns: w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)
a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

answer = []
# 3차원 dp 배열을 생성한다.
dp = [[[1]*21 for _ in range(21)] for _ in range(21)]
# 0 <= a, b, c <= 20 일때의 w(a,b,c) 에 의한 결과값을 계산, 저장한다.
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

while True:
    a, b, c = map(int, input().split())
    tmp = 0
    if a == b == c == -1:
        break
    elif a <= 0 or b <= 0 or c <= 0:
        tmp = dp[0][0][0]
    elif a > 20 or b > 20 or c > 20:
        tmp = dp[20][20][20]
    else:
        tmp = dp[a][b][c]
    answer.append("w({}, {}, {}) = {}".format(a, b, c, tmp))

print(*answer, sep = '\n')

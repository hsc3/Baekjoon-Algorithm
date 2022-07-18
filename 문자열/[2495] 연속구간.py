'''
[2495] 연속구간 / Bronze 2 / 문자열, 다이나믹 프로그래밍
여덟 자리의 양의 정수가 주어질 때, 그 안에서 연속하여 같은 숫자가 나오는 것이 없으면 1을 출력하고, 있으면 같은 숫자가 연속해서 나오는 구간 중 가장 긴 것의 길이를 출력하는 프로그램을 작성하라.
예를 들어 세 개의 숫자 12345123, 17772345, 22233331이 주어졌다고 하자. 12345123은 연속하여 같은 숫자가 나오는 것이 없으므로 1을 출력하고,
17772345는 7이 세 개 연속하여 나오므로 3을 출력하며, 22233331의 경우에는 2가 세 개, 3이 네 개 연속해서 나오므로 그 중 큰 값인 4를 출력하여야 한다.
'''
import sys 
input = sys.stdin.readline

answer = []
for _ in range(3):
    number = input().rstrip()
    maxCnt = 0
    cnt = 0
    for i in range(len(number)-1):
        if number[i] != number[i+1]: # 뒤의 숫자와 같지 않은 경우
            maxCnt = max(cnt+1, maxCnt)
            cnt = 0
        else:
            cnt += 1
    maxCnt = max(cnt + 1, maxCnt)
    answer.append(maxCnt)

print(*answer, sep='\n')

# answer = []
# for _ in range(3):
#     number = input().rstrip()
#     dp = [1] * 8
#
#     for i in range(len(number)-1):
#         if number[i] == number[i+1]:
#             dp[i+1] += dp[i]
#
#     answer.append(max(dp))
#
# print(*answer, sep='\n')

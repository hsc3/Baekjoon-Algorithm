# [9251] LCS | Gold 5 | 다이나믹 프로그래밍, 문자열
'''
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다. 입력으로 주어진 두 문자열의 LCS의 길이를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
A = input().rstrip()
B = input().rstrip()
lenA, lenB = len(A), len(B)
dp = [0] * lenB

for i in range(lenA):
    commonLength = 0 # A[:i+1] 와 B[:j+1]의 LCS의 길이
    for j in range(lenB):
        if commonLength < dp[j]:
            commonLength = dp[j]
        elif A[i] == B[j]: # 같은 문자인 경우, LCS의 길이를 1 증가
            dp[j] = commonLength + 1

print(max(dp))

# dp = [[0 for _ in range(1001)] for _ in range(1001)]
#
# for i in range(len(A)):
#     for j in range(len(B)):
#         dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], dp[i][j] + (A[i] == B[j]))
#
# print(dp[len(A)][len(B)])
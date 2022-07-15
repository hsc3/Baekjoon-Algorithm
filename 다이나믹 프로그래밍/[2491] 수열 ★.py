'''
[2491] 수열 / Silver 4 / 다이나믹 프로그래밍
0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다. 그 수열 안에서 연속해서 커지거나(같은 것 포함),
혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램을 작성하라.
예를 들어 수열 1, 2, 2, 4, 4, 5, 7, 7, 2 의 경우에는 1 ≤ 2 ≤ 2 ≤ 4 ≤ 4 ≤ 5 ≤ 7 ≤ 7 이 가장 긴 구간이 되므로 그 길이 8을 출력한다.
수열 4, 1, 3, 3, 2, 2, 9, 2, 3 의 경우에는 3 ≥ 3 ≥ 2 ≥ 2 가 가장 긴 구간이 되므로 그 길이 4를 출력한다.
또 1, 5, 3, 6, 4, 7, 1, 3, 2, 9, 5 의 경우에는 연속해서 커지거나 작아지는 수열의 길이가 3 이상인 경우가 없으므로 2를 출력하여야 한다.
'''
n = int(input())
numbers = list(map(int, input().split()))

# 오름차순의 경우와 내림차순의 경우를 각각 저장
ascending = [1 for _ in range(n)] # 같거나 증가
descending = [1 for _ in range(n)] # 같거나 감소

for i in range(1, n):
  # 오름차순 여부
  if numbers[i-1] <= numbers[i]: 
    ascending[i] += ascending[i-1]
  else: 
    ascending[i] = 1

  # 내림차순 여부
  if numbers[i-1] >= numbers[i]:
    descending[i] += descending[i-1]
  else: 
    descending[i] = 1

print(max(max(ascending), max(descending)))

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = list(map(int, input().split()))
# if N == 1 :
#     print(1)
#     exit(0)
#
# dp = [1]*N
# dp[1] = 2
#
# for i in range(2, N):
#
#     if arr[i-1] == arr[i]:
#         dp[i] += dp[i-1]
#
#     elif arr[i-1] < arr[i]:
#         if arr[i-2] < arr[i-1]:
#             dp[i] += dp[i-1]
#         elif arr[i-2] > arr[i-1]:
#             dp[i] = 2
#         else:
#             cnt = 0
#             for j in range(i,0,-1):
#                 if arr[j-1] <= arr[j]:
#                     cnt += 1
#                 else:
#                     break
#             dp[i] = cnt + 1
#
#     else: # arr[i-1] > arr[i]
#         if arr[i-2] > arr[i-1]:
#             dp[i] += dp[i-1]
#         elif arr[i-2] < arr[i-1]:
#             dp[i] = 2
#         else:
#             cnt = 0
#             for j in range(i, 0, -1):
#                 if arr[j-1] >= arr[j]:
#                     cnt += 1
#                 else:
#                     break
#             dp[i] = cnt + 1
#
# print(max(dp))

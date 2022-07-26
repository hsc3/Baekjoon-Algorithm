# [20551] Sort 마스터 배지훈의 후계자 / Silver 4 / 이분 탐색, 자료구조(map)
'''
지훈이는 Sort 마스터다. 오랫동안 Sort 마스터 자리를 지켜온 지훈이는 이제 마스터 자리를 후계자에게 물려주려고 한다.
수많은 제자들 중에 후계자를 고르기 위해서 지훈이는 제자들에게 문제를 준비했다.
먼저 제자들에게 N개의 원소를 가진 배열 A를 주고, A의 원소들이 오름차순으로 정렬된 배열 B를 만들게 한다.
그다음 M개의 질문을 한다. 각 질문에는 정수 D가 주어진다. 제자들은 주어진 정수 D가 B에서 가장 먼저 등장한 위치를 출력하면 된다.
단, D가 B에 존재하지 않는 경우에는 -1를 출력한다.
Sort 마스터의 자리를 너무나도 물려받고 싶은 창국이를 위해 지훈이의 문제를 풀 수 있는 프로그램을 만들어 주자.
'''
# 1. 이분 탐색법 활용
import sys
input = sys.stdin.readline
from bisect import bisect_left

N, M = map(int, input().split())
A = sorted(list(int(input()) for _ in range(N)))

answer = []
for _ in range(M):
    findNum = int(input())
    idx = bisect_left(A, findNum) # 배열 안에서 찾는 숫자의 가장 왼쪽 인덱스
    if idx < N and A[idx] == findNum:
        answer.append(idx)
    else:
        answer.append(-1)

print(*answer, sep='\n')

# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# A = sorted([int(input()) for _ in range(N)])
#
# # 이분 탐색 (lower bound)
# answer = []
# for _ in range(M):
#     findNum = int(input()) # 찾고자 하는 숫자
#     findIdx = -1 # 찾는 숫자의 인덱스
#     left, right = 0, N
#
#     while True:
#         if left >= right:
#             break
#
#         mid = (left + right) // 2
#         if A[mid] >= findNum: # 찾고자 하는 숫자보다 크거나 같은 경우(중복 숫자가 앞에 있을 수 있으므로 다시 탐색한다)
#             if A[mid] == findNum:
#                 findIdx = mid
#             right = mid
#         else: # 찾고자 하는 숫자보다 작은 경우
#             left = mid + 1
#     answer.append(findIdx)
#
# print(*answer, sep = '\n')

# 2. 맵 활용
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# A = sorted(list(int(input()) for _ in range(N)))
# B = dict()
# for i in range(len(A)): # 숫자가 등장하는 (가장 빠른) 위치를 저장합니다.
#     try:
#         B[A[i]]
#     except:
#         B[A[i]] = i
#
# answer = []
# for _ in range(M): # 숫자의 위치를 찾습니다.
#     findNum = int(input())
#     try:
#         answer.append(B[findNum])
#     except:
#         answer.append(-1)
#
# print(*answer, sep='\n')

# [6198] 옥상 정원 꾸미기 | Gold 5 | https://www.acmicpc.net/problem/6198

import sys
input = sys.stdin.readline

N = int(input())
buildings = list(int(input()) for _ in range(N))
stk = []

answer = 0
for i in range(N):
    while stk and stk[-1] < buildings[i]: # 뒤의 빌딩의 높이가 더 높거나 같은 경우
        stk.pop() # 이전 빌딩들은 스택에서 제거
    stk.append(buildings[i]) # 뒤의 해당 빌딩을 스택에 추가
    answer += (len(stk)-1) # 가장 높은 빌딩에서 볼 수 있는 옥상의 수를 누적

print(answer)

'''
[10, 3]
[10, 7]
[10, 7, 4]
[12, 2]
'''


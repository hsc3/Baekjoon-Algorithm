# [2659] 십자카드 문제 | Silver 3 | https://www.acmicpc.net/problem/2659

import sys
from collections import deque
input = sys.stdin.readline

def makeClockNumber(number):
    number = deque(map(str, str(number).rstrip()))
    clockNumber = float("inf")
    for _ in range(4):
        number.rotate(-1) # 시계방향 회전
        tmp = int(''.join(number))
        clockNumber = min(clockNumber, tmp)

    return clockNumber

myClockNumber = makeClockNumber(int(''.join(map(str, input().split()))))

answer = 1
for i in range(1111, int(myClockNumber)): # clockNumber 이전의 시계수가 몇 개 있는지 체크
    if '0' not in str(i) and makeClockNumber(i) == i:
        answer += 1

print(answer)
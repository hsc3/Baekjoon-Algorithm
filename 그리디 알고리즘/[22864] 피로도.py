# [22864] 피로도 | Bronze 2 | https://www.acmicpc.net/problem/22864
import sys
input = sys.stdin.readline

tiredness = 0 # 피로도
answer = 0 # 일의 양
hour = 0

A, B, C, M = map(int, input().split()) # 24시간동안 피로도가 M을 넘지 않도록 최대한 많은 일을 하라.

while hour < 24:
    if tiredness + A > M: # 피로도가 M을 넘는 경우 -> 쉬어야 한다.
        tiredness -= (C if C <= tiredness else tiredness)
    else: # 피로도가 M을 넘지 않는 경우 -> 일을 한다.
        tiredness += A
        answer += B
    hour += 1

print(answer)
# [15501] 부당한 퍼즐 / Silver 3 / Deque

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
original = deque(map(int, input().split())) # 기존 문자열
result = deque(map(int, input().split())) # 결과 문자열

if N > 1 :
    # reverse 여부 파악 
    if original.index(result[0]) > original.index(result[1]) :
        original.reverse()

    # rotate 
    rotate_cnt = original.index(result[0])
    original.rotate(-rotate_cnt) if rotate_cnt <= N else original.rotate(rotate_cnt)

print("good puzzle") if original == result else print("bad puzzle")
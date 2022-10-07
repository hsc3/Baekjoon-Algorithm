# [2869] 달팽이는 올라가고 싶다 | Silver 5 | https://www.acmicpc.net/problem/2869
import sys
input = sys.stdin.readline
from math import ceil

A, B, V = map(int, input().split())
# A : 낮에 A 미터만큼 올라감
# B : 밤에 B 미터만큼 떨어짐
# V : V 미터만큼 올라가야 함

print(ceil((V-A)/(A-B)) + 1)
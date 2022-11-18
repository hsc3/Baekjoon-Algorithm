# [16435] 스네이크버드 | Silver 5 | https://www.acmicpc.net/problem/16435
import sys
input = sys.stdin.readline

N, L = map(int, input().split()) # 과일의 수, 스네이크버드의 초기 길이
fruits = sorted(list(map(int, input().split()))) # 오름차순 정렬

for fruit in fruits:
    if L >= fruit: # 몸의 길이 이하의 높이에 과일이 있으면 먹는다.
        L += 1

print(L)
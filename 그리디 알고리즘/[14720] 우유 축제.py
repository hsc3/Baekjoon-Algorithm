# [14720] 우유 축제 | Bronze 3 | https://www.acmicpc.net/problem/14720
import sys
input = sys.stdin.readline

answer = 0

N = int(input())
store = list(map(int, input().split()))
choice = 0

for milk in store:
    if milk == choice:
        answer += 1
        choice += 1
        if choice == 3:
            choice = 0

print(answer)
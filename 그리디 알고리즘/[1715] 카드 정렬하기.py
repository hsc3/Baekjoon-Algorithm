# [1715] 카드 정렬하기 | Gold 4 | https://www.acmicpc.net/problem/1715
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

answer = 0

N = int(input())
cards = []
for _ in range(N):
    heappush(cards, int(input()))

while len(cards) >= 2:
    cardSum = heappop(cards) + heappop(cards)
    answer += cardSum
    heappush(cards, cardSum)

print(answer)

'''
[10 20 30 40] answer = 0
[30 30 40] answer = 30
[40 60] answer = 90
[100] answer = 190
'''
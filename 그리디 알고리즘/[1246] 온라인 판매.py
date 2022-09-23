# [1246] 온라인 판매 | Silver 4 | https://www.acmicpc.net/problem/1246

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = sorted([int(input()) for _ in range(M)], reverse=True) # 손님의 달걀 구매 가격을 내림차순 정렬 (달걀 가격이 P를 넘으면 손님은 달걀을 사지 않는다.)
# P = [10, 8, 7, 2]

maximum = P[0] # 최대 달걀 판매 수익
price = P[0] # 달걀 판매 가격
for i in range(1, min(N, M)): # 계란이 남아도 손님이 없으면 판매X, 손님이 있어도 계란이 없으면 판매X
    profit = P[i] * (i+1)
    if maximum < profit: # 최대 달걀 판매 수익 갱신
        maximum = profit
        price = P[i]

print(price, maximum)
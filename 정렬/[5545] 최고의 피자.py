# [5545] 최고의 피자 | Silver 3 | https://www.acmicpc.net/problem/5545
import sys
input = sys.stdin.readline

# 토핑을 k개 선택했을때, 1원당 열량이 가장 높은 피자를 구한다.
answer = 0 # 1원당 최대 열량

N = int(input()) # 토핑의 종류의 수
A, B = map(int, input().split()) # 도우, 토핑의 가격
C = int(input()) # 도우의 열량
D = sorted(list(int(input()) for _ in range(N)), reverse=True) # 토핑의 열량 (내림차순 정렬)

for k in range(N+1):
    calories = C + sum(D[:k]) # 총 열량 = 도우의 열량 + k개의 토핑의 열량
    price = A + (B * k) # 총 가격
    answer = max(answer, calories // price)

print(answer)

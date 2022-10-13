# [15961] 회전 초밥 | Gold 4 | https://www.acmicpc.net/problem/15961
import sys
input = sys.stdin.readline
from collections import defaultdict

N, d, k, c = map(int, input().split()) # N: 벨트에 놓인 접시 수, d: 초밥의 가지수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호
sushi = [int(input()) for _ in range(N)]
sushi += sushi[:k-1]


left, right = 0, k
eating = defaultdict(int)
for i in range(left, right):
    eating[sushi[i]] += 1

answer = [] # 초밥의 가짓수를 저장

while right < len(sushi)-1:
    answer.append(len(eating) + (1 if c not in eating.keys() else 0)) # 쿠폰 번호의 초밥을 추가한 가짓수 저장
    eating[sushi[right]] += 1 # 오른쪽의 초밥 추가
    eating[sushi[left]] -= 1  # 왼쪽의 초밥 제거

    if eating[sushi[left]] == 0:
        eating.pop(sushi[left])

    right += 1
    left += 1

print(max(answer))
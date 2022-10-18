# [2961] 도영이가 만든 맛있는 음식 | Silver 2 | https://www.acmicpc.net/problem/2961
import sys
input = sys.stdin.readline

def Cook(ingredients): # 요리 맛 계산
    sourTaste = 1
    bitterTaste = 0
    for ingredient in ingredients:
        sourTaste *= sour[ingredient]
        bitterTaste += bitter[ingredient]

    return abs(sourTaste - bitterTaste)

from itertools import combinations

answer = []
sour = []
bitter = []
N = int(input())
for _ in range(N):
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)

for i in range(1, N+1): # 재료 갯수
    for ingredients in combinations([n for n in range(N)], i): # 모든 재료 조합
        answer.append(Cook(ingredients))

print(min(answer))

# def Choose(i, ingredients): # 재료 선택
#     global answer
#     if len(ingredients) > 0:
#         answer.append(Cook(ingredients))
#
#     for idx in range(i, N):
#         Choose(idx+1, ingredients + [idx])
#
# if __name__ == "__main__":
#     sour = []
#     bitter = []
#     N = int(input())
#     for _ in range(N):
#         s, b = map(int, input().split())
#         sour.append(s)
#         bitter.append(b)
#
#     answer = []
#     Choose(0, [])
#
#     print(min(answer))
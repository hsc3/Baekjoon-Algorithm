# [13904] 과제 | Gold 3 | https://www.acmicpc.net/problem/13904
import sys
input = sys.stdin.readline
from heapq import heappop, heappush


N = int(input())
answer = [0 for _ in range(N+1)]

homework = []
for _ in range(N): # 과제 점수를 기준으로 내림차순 정렬
    day, score = map(int, input().split())
    heappush(homework, [-score, day])

while homework: # 점수가 높은 과제를 우선으로, 마감일 이전에 완료한다.
    score, day = heappop(homework)
    for i in range(day, 0, -1):
        if i <= N and answer[i] == 0: # 마감일 이전에, 해당 과제를 수행할 수 있는 경우
            answer[i] = -score
            break

print(sum(answer))
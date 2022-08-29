# [14235] 크리스마스 선물 | Silver 3 | 자료구조(Heap)
'''
크리스마스에는 산타가 착한 아이들에게 선물을 나눠준다. 올해도 산타는 선물을 나눠주기 위해 많은 노력을 하고 있는데, 전세계를 돌아댕기며 착한 아이들에게 선물을 나눠줄 것이다.
하지만 산타의 썰매는 그렇게 크지 않기 때문에, 세계 곳곳에 거점들을 세워 그 곳을 방문하며 선물을 충전해 나갈 것이다. 또한, 착한 아이들을 만날 때마다 자신이 들고있는 가장 가치가 큰 선물 하나를 선물해 줄 것이다.
이제 산타가 선물을 나눠줄 것이다. 차례대로 방문한 아이들과 거점지의 정보들이 주어졌을 때, 아이들에게 줄 선물들의 가치들을 출력하시오. 만약 아이들에게 줄 선물이 없다면 -1을 출력하시오.
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input()) # 아이들과 거점지를 방문한 횟수
present = [] # 산타가 가지고 있는 선물의 가치

answer = []
for _ in range(N):
    A = list(map(int, input().split())) # 아이 방문(0) or 선물 충전([선물의 가치])
    # 1. 아이 방문
    if A[0] == 0:
        if present: # 선물이 있는 경우 -> 가장 가치있는 선물 전달
            answer.append(-heappop(present))
        else: # 선물이 없는 경우 -> -1 저장
            answer.append(-1)
    # 2. 선물 충전
    else:
        for present_worth in A[1:]:
            heappush(present, -present_worth)

print(*answer, sep='\n')
        

# [23253] 자료구조는 정말 최고야 | Silver 5 | 자료구조(Heap)
'''
N권의 교과서는 각각 1부터 N까지의 번호가 매겨져 있다. 찬우는 각 더미의 맨 위에 있는 교과서만 꺼낼 수 있으며, 반드시 교과서를 꺼낸 순서대로 나열해야 하기 때문에
번호순으로 나열하기 위해서는 1번, 2번, … N - 1번, N번 교과서 순으로 꺼내야 한다. 교과서를 올바르게 나열할 수 없다면 중간고사 공부를 때려치겠다는 찬우를 위해
번호순으로 나열할 수 있는지 여부를 알려주는 프로그램을 작성해 주자. (올바른 순서대로 교과서를 꺼낼 수 있다면 Yes를, 불가능하다면 No를 출력한다.)
'''
from heapq import heappush, heappop
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dummies = []

for _ in range(M):
    K = int(input())
    book = deque(list(map(int, input().split()))[::-1])
    heappush(dummies, book) # 각 더미를 힙에 넣어주고, 힙 정렬 수행 (더미의 첫 번째 원소 기준)

num = 1
flag = True
while num <= N:
    dummy = heappop(dummies) # 가장 번호가 빠른 교과서를 가진 더미 탐색
    book_num = dummy.popleft()
    if book_num == num: # 찾는 교과서 번호와 일치하는 경우
        if dummy:
            heappush(dummies, dummy) # 해당 교과서를 제외하고, 다시 힙에 넣어준다.
        num += 1
    else:
        flag = False
        break

print("Yes" if flag else "No")

# # 각각의 더미가 내림차순 정렬되어 있어야, 모든 교과서를 번호순으로 나열할 수 있다.
# N, M = map(int, input().split())
# for _ in range(M):
#     K = map(int, input().split())
#     dummy = list(map(int, input().split()))
#     if dummy != sorted(dummy, reverse = True):
#         print("No")
#         exit(0)
# print("Yes")
'''
[1697] 숨바꼭질 | Silver 1 | 그래프 (BFS)
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
(수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.)
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split()) # 수빈, 동생의 위치
cost = [0 for _ in range(100001)]
def BFS(n, k) :
    q = deque()
    q.append(n)
    while q:
        n = q.popleft()
        if n == k : break
        # 해당 지점에 가장 먼저 도착하는 시간만을 저장합니다.
        if n+1 <= 100000 and cost[n+1] == 0 : # X+1로 이동
            cost[n+1] = cost[n] + 1
            q.append(n+1)
        if n-1 >= 0 and cost[n-1] == 0 : # X-1로 이동
            cost[n-1] = cost[n] + 1
            q.append(n-1)
        if 2*n <= 100000 and cost[2*n] == 0: # 순간이동
            cost[2*n] = cost[n] + 1
            q.append(2*n)
BFS(n, k)
print(cost[k])
# [11060] 점프 점프 | Silver 2 | 그래프, 다이나믹 프로그래밍
'''
재환이가 1×N 크기의 미로에 갇혀있다. 미로는 1×1 크기의 칸으로 이루어져 있고, 각 칸에는 정수가 하나 쓰여 있다.
i번째 칸에 쓰여 있는 수를 Ai라고 했을 때, 재환이는 Ai이하만큼 오른쪽으로 떨어진 칸으로 한 번에 점프할 수 있다. 예를 들어, 3번째 칸에 쓰여 있는 수가 3이면, 재환이는 4, 5, 6번 칸 중 하나로 점프할 수 있다.
재환이는 지금 미로의 가장 왼쪽 끝에 있고, 가장 오른쪽 끝으로 가려고 한다. 이때, 최소 몇 번 점프를 해야 갈 수 있는지 구하는 프로그램을 작성하시오. 만약, 가장 오른쪽 끝으로 갈 수 없는 경우에는 -1을 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [float("inf") for _ in range(N)] # 점프 횟수
dp[0] = 0

q = deque([0])
while q:
    prev = q.popleft() # 현재 위치

    for jump in range(1, A[prev]+1): # 점프할 수 있는 범위
        next = prev + jump # 다음 위치
        if next < N and dp[prev]+1 < dp[next]: # 더 적게 점프해서 갈 수 있는 경우, 다음 위치 탐색
            dp[next] = dp[prev] + 1
            q.append(next)

print(-1 if dp[N-1] == float("inf") else dp[N-1])
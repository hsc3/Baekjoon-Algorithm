# [9657] 돌 게임 (3) | Silver 3 | https://www.acmicpc.net/problem/9657
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (1001)
dp[1] = 0 # 상근 승리
dp[2] = 1 # 창영 승리
dp[3] = 0
dp[4] = 0

# 우선권은 상근이에게 있다.
for i in range(5, N+1):
    if dp[i-1] == 1 or dp[i-3] == 1 or dp[i-4] == 1:
        dp[i] = 0 # 상근이가 승리할 수 있는 경우 (한 번의 라운드가 적은 케이스에서, 창영이가 이긴 경우가 1번이라도 있으면 상근이가 무조건 승리한다.)
    else:
        dp[i] = 1 # 상근이가 승리할 수 없는 경우

print("SK" if dp[N] == 0 else "CY")
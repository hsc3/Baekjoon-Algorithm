# [2828] 사과 담기 게임 | Silver 5 | 그리디 알고리즘
'''
스크린은 N칸으로 나누어져 있다. 스크린의 아래쪽에는 M칸을 차지하는 바구니가 있다. (M<N)
플레이어는 게임을 하는 중에 바구니를 왼쪽이나 오른쪽으로 이동할 수 있다. 하지만, 바구니는 스크린의 경계를 넘어가면 안 된다. 가장 처음에 바구니는 왼쪽 M칸을 차지하고 있다.
스크린의 위에서 사과 여러 개가 떨어진다. 각 사과는 N칸중 한 칸의 상단에서 떨어지기 시작하며, 스크린의 바닥에 닿을때까지 직선으로 떨어진다. 한 사과가 바닥에 닿는 즉시, 다른 사과가 떨어지기 시작한다.
바구니가 사과가 떨어지는 칸을 차지하고 있다면, 바구니는 그 사과가 바닥에 닿을 때, 사과를 담을 수 있다. 상근이는 사과를 모두 담으려고 한다. 이때, 바구니의 이동 거리의 최솟값을 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 바닥, 바구니
apples = [int(input()) for _ in range(int(input()))]

# 바구니를 최소한으로 움직인다. -> 바구니의 경계에 사과가 담기도록 한다.
answer = 0
baguni_left = 1
baguni_right = M
for apple in apples:
    if baguni_left <= apple <= baguni_right: # 사과가 바구니의 안쪽에 떨어지고 있는 경우
        continue
    else:
        if apple < baguni_left: # 사과가 바구니의 왼쪽에 떨어지는 경우
            move = apple - baguni_left # 왼쪽으로 이동해야하는 최소 거리

        elif baguni_right < apple: # 사과가 바구니의 오른쪽에 떨어지는 경우
            move = apple - baguni_right # 오른쪽으로 이동해야하는 최소 거린

        baguni_left += move
        baguni_right += move
        answer += (move if move > 0 else -move)

print(answer)
        


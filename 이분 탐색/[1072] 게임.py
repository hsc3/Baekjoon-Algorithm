# [1072] 게임 | Silver 3 | 이분 탐색
'''
형택이는 앞으로의 모든 게임에서 지지 않는다. 게임 기록은 다음과 같이 생겼다.
- 게임 횟수 : X
- 이긴 게임 : Y (Z%)
Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.
'''

X, Y = map(int, input().split())
Z = (Y * 100) // X # 기존 승률

start, end = 1, 100000000000 # 또는 end = X+1
answer = float("inf")

while start < end:
    mid = (start + end) // 2 # 더 하는 게임 수
    newZ = ((Y + mid) * 100) // (X + mid) # 새로운 승률

    if newZ >= Z + 1: # 새로운 승률이 기존 승률보다 1% 이상 높은 경우
        answer = min(answer, mid) # 저장하고 lower_bound 탐색 (최소 게임 수를 탐색한다.)
        end = mid
    elif newZ < Z + 1:
        start = mid + 1

print(answer if answer != float("inf") else -1)
'''
[1446] 지름길 / Silver 1 / 다이나믹 프로그래밍
어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.
세준이가 운전해야 하는 거리의 최솟값을 출력하시오.
첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다.
'''
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
shortcut = [list(map(int, input().split())) for _ in range(N)]
shortcut.sort()
# 0 50 10
# 0 50 20
# 50 100 10
# 100 151 10
# 110 140 90

dp = [i for i in range(D+1)] # 고속도로의 i 지점에 도달하는 거리 (지름길x)

for start, end, distance in shortcut : 
    for i in range(end, D+1) : # 지름길이 존재할 경우, 지름길 이후의 지점 i에 대한 거리 업데이트
        dp[i] = min(dp[start] + distance + (i-end), dp[i]) # 
        # (지름길 시작 지점 - 끝나는 지점)의 거리 + (지름길 끝나는 지점 - i 지점)까지의 거리

print(dp[D])

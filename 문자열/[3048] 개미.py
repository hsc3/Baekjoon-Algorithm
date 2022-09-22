# [3048] 개미 | Silver 4 | https://www.acmicpc.net/problem/3048
import sys
input = sys.stdin.readline

N1, N2 = map(int, input().split())
ant1 = list(map(str, input().rstrip()))[::-1]
ant2 = list(map(str, input().rstrip()))
ants = ant1 + ant2
move = [False for _ in range(N1+N2)] # 움직였는지 여부 기록

T = int(input())
for _ in range(T):
    for i in range(N1+N2-1): # 왼쪽 개미들을 -> 방향으로 움직인다.
        if ants[i] in ant1 and ants[i+1] in ant2 and move[i] == False and move[i+1] == False:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            move[i] = True
            move[i+1] = True

    for i in range(N1+N2-1, 0, -1): # 오른쪽 개미들을 <- 방향으로 움직인다.
        if ants[i-1] in ant1 and ants[i] in ant2 and move[i-1] == False and move[i] == False:
            ants[i-1], ants[i] = ants[i], ants[i-1]
            move[i-1] = True
            move[i] = True
    move = [False for _ in range(N1+N2)] # T초에서의 움직임 초기화


print(''.join(ants))

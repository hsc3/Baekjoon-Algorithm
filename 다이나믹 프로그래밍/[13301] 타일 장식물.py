# [13301] 타일 장식물 | Silver 5 | https://www.acmicpc.net/problem/13301

N = int(input())
tile = [0, 1] + [0] * (N-1)
for i in range(2, N+1):
    tile[i] = tile[i-2] + tile[i-1]

print(tile[N] * 4 + tile[N-1] * 2)
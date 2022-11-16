# [9322] 철벽 보안 알고리즘 | Silver 4 | https://www.acmicpc.net/problem/9322
import sys
input = sys.stdin.readline

answer = []

T = int(input())
for _ in range(T):
    N = int(input())

    first_open_key = dict()
    for key, value in enumerate(list(map(str, input().split()))): # 제 1 공개키
        first_open_key[value] = key

    pattern = []
    for key in list(map(str, input().split())): # 제 2 공개키
        pattern.append(first_open_key[key])

    cryptogram = list(map(str, input().split()))

    tmp = [' '] * N
    for i in range(N):
        tmp[pattern[i]] = cryptogram[i]
    answer.append(' '.join(tmp))

print(*answer, sep='\n')
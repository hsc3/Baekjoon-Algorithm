# [25305] 커트라인 | Bronze 2 | https://www.acmicpc.net/problem/25305
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
score = sorted(list(map(int, input().split())), reverse=True)
print(score[K-1])
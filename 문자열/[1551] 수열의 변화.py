# [1551] 수열의 변화 | Bronze 1 | https://www.acmicpc.net/problem/1551
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split(',')))
for _ in range(K):
    arr = [arr[i] - arr[i-1] for i in range(1, len(arr))]

print(*arr, sep=',')
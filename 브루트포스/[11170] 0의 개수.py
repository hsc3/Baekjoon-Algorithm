# [11170] 0의 개수 | Bronze 1 | https://www.acmicpc.net/problem/11170
import sys
input = sys.stdin.readline

def countZero(N, M):
    count = 0
    for i in range(N, M+1):
        count += str(i).count('0')
    return count


def solution():
    answer = []

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        answer.append(countZero(N, M))

    print(*answer, sep='\n')

solution()
# [2702] 초6 수학 | Bronze 2 | https://www.acmicpc.net/problem/2702
import sys
input = sys.stdin.readline

def LCM(a, b): # 최소공배수
    i = 1
    while True:
        if (a * i) % b == 0:
            return a * i
        i += 1

def GCD(a, b): # 최소공약수
    if b == 0:
        return a
    return GCD(b, a % b)


def solution():
    answer = []

    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        answer.append([LCM(a, b), GCD(a, b)])

    for a in answer:
        print(*a)

solution()
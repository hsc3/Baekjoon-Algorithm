# [1978] 소수 찾기 | Silver 5 | https://www.acmicpc.net/problem/1978
import sys
input = sys.stdin.readline
from math import sqrt

def findPrimeNumber(N1, N2):
    for i in range(2, int(sqrt(N2))+1):
        if not ckecked[i]:
            for num in range(2*i, N2+1, i):
                ckecked[num] = True

    answer = 0
    for num in numbers:
        if not ckecked[num]:
            answer += 1

    return answer

N = int(input())
numbers = list(map(int, input().split()))
N1, N2 = min(numbers), max(numbers)
ckecked  = [True, True] + [False for _ in range(N2-1)]
print(findPrimeNumber(N1, N2))


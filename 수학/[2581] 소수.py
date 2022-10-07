# [2581] 소수 | Silver 5 | https://www.acmicpc.net/problem/2581
from math import sqrt

def findPrimeNumbers(M, N):
    checked = [True, True] + [False] * (N-1)

    for i in range(2, int(sqrt(N))+1):
        if not checked[i]:
            for num in range(2*i, N+1, i):
                checked[num] = True

    prime_numbers = []

    for num in range(M, N+1):
        if not checked[num]:
            prime_numbers.append(num)

    return prime_numbers

M = int(input())
N = int(input())
pn = findPrimeNumbers(M, N)

if not pn:
    print(-1)
else:
    print(sum(pn), min(pn))
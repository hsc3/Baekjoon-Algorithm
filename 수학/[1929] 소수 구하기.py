# [1929] 소수 구하기 | Silver 3 | https://www.acmicpc.net/problem/1929

M, N = map(int, input().split())
is_prime = [False, False] + [True] * (N-1)
primes = []
for i in range(2, N+1):
    if is_prime[i]:
        if i >= M:
            primes.append(i)

        for j in range(2*i, N+1, i):
            is_prime[j] = False

print(*primes, sep='\n')
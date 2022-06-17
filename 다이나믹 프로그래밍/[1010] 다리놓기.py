'''
[1010] 다리놓기  |  https://www.acmicpc.net/problem/1010
서쪽의 사이트(N)와 동쪽의 사이트(M)를 다리로 연결하려고 한다. (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.)
다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다. 
다리끼리는 서로 겹쳐질 수 없다고 할 때, 다리를 최대로 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
'''

'''
# 수학 
import sys, math
from math import comb
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    N, M = map(int, input().split()) # 서쪽, 동쪽 사이트의 수
    if N >= M : print(comb(N,M))
    else : print(comb(M,N))
'''

# Top-Down Dynamic Programming
T = int(input())
cache = [[-1] * 30 for _ in range(30)]

def solve(m, n):
    if n == 0 or m == n:
        return 1
    if cache[m][n] != -1:
        return cache[m][n]

    cache[m][n] = solve(m - 1, n - 1) + solve(m - 1, n)
    return cache[m][n]

for _ in range(T):
    N, M = map(int, input().split())
    print(solve(M, N))

'''
[1059] 좋은 구간 / Silver 5 / 브루트포스, 정렬
정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.
- A와 B는 양의 정수이고, A < B를 만족한다.
- A ≤ A ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.
'''
import sys
from itertools import product
input = sys.stdin.readline

res = 0

L = int(input()) # 집합 S의 크기
S = [0] + sorted(list(map(int, input().split()))) + [1000] # S = [0, 4, 8, 13, 24, 30, 1000]
n = int(input()) # 10

A, B = 0, 0
goodSection = False
for i in range(len(S)-1) :
    if S[i] < n < S[i+1] :
        A = S[i] + 1  # A = 9
        B = S[i+1] # B = 13
        goodSection = True
        break

if not goodSection :
    print(0)
    exit(0)

xCandidate = [xc for xc in range(A, n+1)] # [9, 10]
yCandidate = [yc for yc in range(n, B)] # [10, 11, 12]

for gs in product(xCandidate, yCandidate) :
    if gs[0] < gs[1] :
        res += 1 # [9, 10], [9, 11], [9, 12], [10, 11], [10, 12]

print(res)
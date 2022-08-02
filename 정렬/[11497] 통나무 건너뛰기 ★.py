# [11497] 통나무 건너뛰기 | Silver 1 | 정렬
'''
N개의 통나무를 원형으로 세워 놓고 뛰어놀려고 한다. 통나무 건너뛰기의 난이도는 인접한 두 통나무 간의 높이의 차의 최댓값으로 결정된다.
각 테스트 케이스마다 한 줄에 주어진 통나무들로 만들 수 있는 최소 난이도를 출력하시오.
'''
# 내 풀이 : 변형된 리스트의 형태를 만들어서 계산
# 이상적인 풀이 : 변형을 하지 않고, 기존 리스트에서 규칙을 찾아 계산

import sys, itertools
from itertools import permutations
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    tree = sorted(list(map(int, input().split())))
    even_idx = []
    odd_idx = []
    level = []
    for i in range(n) :
        even_idx.append(tree[i]) if i % 2 == 0 else odd_idx.append(tree[i])
    level = even_idx + sorted(odd_idx, reverse = True)

    res = 0
    for i in range(n-1) :
        res = max(res, abs(level[i]-level[i+1]))
    print(res)

'''
a = int(input())
for _ in range(a):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    
    Max = a[1]-a[0]
    
    for i in range(n-2):
        Max = max( Max ,a[i+2]-a[i])
    Max = max(Max, a[len(a)-1]-a[len(a)-2])
    
    print(Max)
'''
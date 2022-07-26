# [17298] 오큰수 | Gold 4 | 자료구조(stack)
'''
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
'''
import sys 
input = sys.stdin.readline
from collections import deque

N = int(input())
data = list(map(int, input().split())) # [3, 5, 2, 7]
res = [-1] * N

stk = deque()

for i in range(N) :
    while stk and stk[-1][0] < data[i] : # 이전에 스택에 넣은 숫자와 비교해서 data[i]가 더 크면, 이전에 스택에 넣은 숫자의 오큰수를 업데이트한다.
        num, idx = stk.pop()
        res[idx] = data[i]
    stk.append([data[i], i])

print(*res)
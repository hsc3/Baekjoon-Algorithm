'''
[18115] 카드 놓기 / Silver 3 / 자료구조(덱)
수현이는 카드 기술을 연습하고 있다. 수현이의 손에 들린 카드를 하나씩 내려놓아 바닥에 쌓으려고 한다. 수현이가 쓸 수 있는 기술은 다음 3가지다.
1. 제일 위의 카드 1장을 바닥에 내려놓는다.
2. 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
3. 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
처음 카드의 상태를 출력하여라.
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())
skills = list(map(int, input().split()))
res = deque()

for num, skill in enumerate(reversed(skills)) :
    if skill == 1 :
        res.appendleft(num+1) 
    elif skill == 2 :
        res.insert(1, num+1)
    else :
        res.append(num+1)

print(' '.join(map(str, res)))
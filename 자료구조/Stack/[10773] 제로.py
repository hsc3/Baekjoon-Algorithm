'''
[10773] 제로 / Silver 4 / 자료구조(스택)
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!
'''
import sys
from collections import deque
input = sys.stdin.readline

stack = deque()

for _ in range(int(input())) :
    num = int(input())
    if num != 0 : # 0이 아닌 숫자인 경우, 스택에 push
        stack.append(num)
    elif stack : # 0을 외쳤고, 스택이 비지 않은 경우, 스택에서 pop
        stack.pop()

print(sum(stack))

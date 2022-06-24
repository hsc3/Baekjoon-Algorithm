'''
[18258] 큐 2 / Silver 4 / 자료구조(덱)
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 여섯 가지이다.
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import deque

N = int(input())
queue = deque()

for _ in range(N) :
    op = list(input().split())
    if op[0] == "push" :
        queue.append(op[1])
    elif op[0] == "pop" :
        print(queue.popleft()+'\n' if queue else '-1\n')
    elif op[0] == "size" :
        print(str(len(queue)) + '\n')
    elif op[0] == "empty" :
        print('0\n' if queue else '1\n')
    elif op[0] == "front" :
        print(queue[0]+'\n' if queue else '-1\n')
    else :
        print(queue[-1]+'\n' if queue else '-1\n')
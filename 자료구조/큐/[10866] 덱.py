'''
[10866] 덱 / Silver 4 / 자료구조(덱)
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오. 
'''
from collections import deque
import sys ; input = sys.stdin.readline

def dequeFunction(operation, operand) :

    global dq

    if operation == "push_front" :
        dq.appendleft(operand)
    elif operation == "push_back" :
        dq.append(operand)
    elif operation == "pop_front" :
        print(-1 if not dq else dq.popleft())
    elif operation == "pop_back" :
        print(-1 if not dq else dq.pop())
    elif operation == "size" :
        print(len(dq))
    elif operation == "empty" :
        print(1 if not dq else 0)
    elif operation == "front" :
        print(-1 if not dq else dq[0])
    elif operation == "back" :
        print(-1 if not dq else dq[-1])


if __name__ == "__main__" :

    dq = deque()

    for _ in range(int(input())) :
        
        inputString = input().rstrip()

        if inputString[:4] == "push" :
            operation, operand = inputString.rsplit()
            dequeFunction(operation, int(operand))
        else :
            dequeFunction(inputString, 0)
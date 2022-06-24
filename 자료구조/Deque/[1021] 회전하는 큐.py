'''
[1021] 회전하는 큐 / Silver 4 / 자료구조(덱)
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.
지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.
1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
원소를 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split()) # 큐의 크기, 뽑아내려고 하는 수의 개수
numbers = list(map(int, input().split())) # 뽑아내려고 하는 수
res = 0

dq = deque(n for n in range(1, N+1))

for number in numbers :
    while True :
        if dq[0] == number : 
            dq.popleft()
            break

        else :
            idx = dq.index(number)
            # left rotation 경우의 수행 횟수
            left_rotation = idx 
            # right rotation 경우의 수행 횟수
            right_rotation = len(dq) - idx

            if left_rotation <= right_rotation :
                dq.rotate(-left_rotation)
                # for _ in range(left_rotation) :
                #     dq.appendleft(dq.pop())
                res += left_rotation
            else : 
                dq.rotate(right_rotation)
                # for _ in range(right_rotation) :
                #    dq.append(dq.popleft())
                res += right_rotation
print(res)

'''
import sys

n, m = map(int, sys.stdin.readline().split())
orders = list(map(int, sys.stdin.readline().split()))
numbers = list(range(1, n+1))

result = 0

for order in orders:
  index = numbers.index(order)
  if index <= len(numbers) // 2 :
    result += index
  else:
    result += len(numbers) - index
  numbers = numbers[index+1:] + numbers[:index]

print(result)
'''
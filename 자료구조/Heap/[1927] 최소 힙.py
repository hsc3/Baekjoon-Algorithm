'''
[1927] 최소 힙 / Silver 2 / 자료 구조(Heap)
널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
- 배열에 자연수 x를 넣는다.
- 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
'''
from heapq import heappop, heappush

N = int(input())
minHeap = []
for _ in range(N) :
    n = int(input())
    if n == 0 :
        print(0) if not minHeap else print(heappop(minHeap))
    else :
        heappush(minHeap, n)

'''
from queue import PriorityQueue
import sys; input = sys.stdin.readline

q = PriorityQueue()
N = int(input()) # 연산의 수
for _ in range(N) :
    n = int(input()) # 명령어 입력
    if n == 0 : # 가장 작은 숫자 출력
        print(0) if q.empty() else print(q.get())
    else : # 숫자 삽입
        q.put(n)
'''
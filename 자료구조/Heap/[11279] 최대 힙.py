'''
[11279] 최대 힙 / Silver 2 / 자료 구조(Heap)
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
- 배열에 자연수 x를 넣는다.
- 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
'''
# heapq는 최소 힙만 지원한다. 
# 수를 음수로 만들어서 저장하면 최대 힙처럼 사용할 수 있다.  
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

maxHeap = []
N = int(input())
for _ in range(N) :
    n = int(input())
    if n == 0 :
        print(0) if not maxHeap else print(-heappop(maxHeap))
    else :
        heappush(maxHeap, -n)

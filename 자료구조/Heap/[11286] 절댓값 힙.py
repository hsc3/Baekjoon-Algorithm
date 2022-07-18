'''
[11286] 절댓값 힙 / Silver 1 / 자료 구조(Heap)
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
- 배열에 정수 x (x ≠ 0)를 넣는다.
- 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
* 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
'''
from heapq import heappush, heappop
from sys import stdin; input = stdin.readline
heap = []
dict = dict()
N = int(input())
for _ in range(N):
    n = int(input())
    if n != 0 :
        dict[abs(n)] = sorted(dict.get(abs(n), list()) + [n])
        heappush(heap, abs(n))
    else :
        if not heap :
            print(0)
        else :
            smallest_abs_num = heappop(heap)
            smallest_num = dict[smallest_abs_num][0]
            if len(dict[smallest_abs_num]) > 1 :
                dict[smallest_abs_num] = dict[smallest_abs_num][1:]
            else :
                dict.pop(smallest_abs_num)
            print(smallest_num)
            print(dict)
'''
import heapq
from sys import stdin
data = []
for _ in range(int(input())):
    n = int(stdin.readline())
    if (n==0):
        if data:
            print(heapq.heappop(data)[1])
        else: print(0)
    else:
        heapq.heappush(data,[abs(n),n])
'''
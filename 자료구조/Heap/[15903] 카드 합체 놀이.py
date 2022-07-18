# [15903] 카드 합체 놀이 / Silver 2 / 자료 구조(Heap)
'''
1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
2. 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.
이 카드 합체를 총 m번 하면 놀이가 끝난다. m번의 합체를 모두 끝낸 뒤, n장의 카드에 쓰여있는 수를 모두 더한 값이 
이 놀이의 점수가 된다. 이 점수를 가장 작게 만드는 프로그램을 작성하자.
'''
import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split()) # 카드의 수, 놀이 횟수
numbers = list(map(int, input().split()))
heapq.heapify(numbers)

for _ in range(M) :
    new_num = heapq.heappop(numbers) + heapq.heappop(numbers)
    heapq.heappush(numbers, new_num)
    heapq.heappush(numbers, new_num)

print(sum(numbers))

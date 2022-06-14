# [10989] 수 정렬하기 (3)
# Bronze 1 >> 정렬
# --------------------------------------------------------------------------------
import sys, heapq
input = sys.stdin.readline

numbers = set()
numbers_check = dict()

for _ in range(int(input())):
    number = int(input())
    numbers.add(number)
    numbers_check[number] = numbers_check.get(number, 0) + 1

numbers = list(numbers)
while numbers:
    heapq.heapify(numbers)
    num = heapq.heappop(numbers)
    for _ in range(numbers_check[num]):
        print(num)
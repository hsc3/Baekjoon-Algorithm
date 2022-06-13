# [2562] 최댓값
# Bronze 2 >> 구현

import heapq, sys
input = sys.stdin.readline

numbers = [[-int(input()), i] for i in range(9)]
heapq.heapify(numbers)
maxNum, idx = heapq.heappop(numbers)
print(-maxNum, idx+1)
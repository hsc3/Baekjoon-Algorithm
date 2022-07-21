# [2562] 최댓값 / Bronze 3 / 구현, 자료구조(Heap)
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

import heapq, sys
input = sys.stdin.readline

numbers = [[-int(input()), i] for i in range(9)] # 숫자와 숫자의 위치를 저장
heapq.heapify(numbers) 
maxNum, idx = heapq.heappop(numbers) # 가장 큰 숫자와 위치를 탐색
print(-maxNum, idx+1)
# [1417] 국회의원 선거 / Silver 5 / 자료구조(Heap)
# Q : 다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램을 작성하시오.
# 표가 많은 사람으로부터 1표씩 가져온다. -> 최대값 ----> Heap
import sys, heapq
input = sys.stdin.readline

vote = []
for _ in range(int(input())) :
    vote.append(-int(input())) # MaxHeap

dasom = -vote.pop(0)
heapq.heapify(vote)
res = 0

while vote :
    max_vote = -heapq.heappop(vote)
    if max_vote < dasom : 
        break
    else :
        dasom += 1
        heapq.heappush(vote, -(max_vote-1))
        res += 1

print(res)
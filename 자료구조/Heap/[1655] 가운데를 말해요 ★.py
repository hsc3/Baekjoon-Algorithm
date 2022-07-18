'''
[1655] 가운데를 말해요 / Gold 2 / 자료 구조(Heap)
동생은 지금까지 백준이가 말한 수 중에서 <<중간값>>을 말해야 한다. 
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.
'''
import sys, heapq
input = sys.stdin.readline

N = int(input())
leftheap = []   # 최대 힙
rightheap = []  # 최소 힙
answer = []

for i in range(N) :
    num = int(input())

    # 숫자 삽입
    if len(leftheap) == len(rightheap) :
        heapq.heappush(leftheap, -num)
    else :
        heapq.heappush(rightheap, num)
    
    # 숫자 재정렬 (swap)
    if rightheap and -leftheap[0] > rightheap[0] :
        heapq.heappush(rightheap, -heapq.heappop(leftheap))
        heapq.heappush(leftheap, -heapq.heappop(rightheap))
    
    answer.append(-leftheap[0])

print(*answer, sep='\n')
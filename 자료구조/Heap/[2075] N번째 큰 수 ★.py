# [2075] N번째 큰 수 | Silver 2 | 자료구조(heap), 정렬
'''
N×N의 표에 수 N2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다. N=5일 때의 예를 보자.
12	7	9	15	5
13	8	11	19	6
21	10	26	31	16
48	14	28	35	25
52	20	32	41	49
이러한 표가 주어졌을 때, N번째 큰 수를 찾는 프로그램을 작성하시오. 표에 채워진 수는 모두 다르다.
'''
import sys 
import heapq
input = sys.stdin.readline
N = int(input())
data = []
reference = [N-1 for _ in range(N)]

for _ in range(N) :
    data.append(list(map(int, input().split())))
maxHeap = [-n for n in data[N-1]]
heapq.heapify(maxHeap)
i = 0
while True :
    max_num = -heapq.heappop(maxHeap)
    max_num_from = data[N-1].index(max_num)
    reference[max_num_from] -= 1
    data[N-1][max_num_from] = data[reference[max_num_from]][max_num_from]
    heapq.heappush(maxHeap, -data[N-1][max_num_from])
    i += 1
    if i == N :
        print(max_num)
        break

'''
heapq는 리스트에 원소를 삽입할 때마다 전부 정렬해주는 것이 아닙니다. 대신 리스트의 제일 앞에 가장 작은 원소가 위치하는 것이 언제나 보장됩니다.

heapq는 나머지 원소들의 위치에 대해선 아무것도 보장해주지 않습니다. 이 원소들의 순서는 각각이 삽입된 순서에 따라서 매우 쉽게 바뀝니다.

삽입 및 삭제의 시간복잡도가 O(logN)인데 언제나 모든 원소가 정렬된 상태이길 원한다면 BBST(Balenced Binary Search Tree)를 사용해야 합니다. 

(C++에선 std::set, std::map이 그 역할)

'''
'''
import sys,heapq
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)

for k in range(n-1): # 4번 실행(4번의 행을 더 입력받을 것.)
    for i in map(int, input().split()):
        if arr[0] < i: # heap의 가장 작은 원소보다 i가 크면 대체한다. 
            heapq.heappop(arr)
            heapq.heappush(arr,i)
# 결과적으로 N*N개의 숫자 중 가장 큰 N개의 숫자가 heap에 담겨있다.
   
print(arr[0])
'''
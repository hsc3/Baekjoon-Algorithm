'''
[7795] 먹을 것인가 먹힐 것인가 | Silver 3 | 이분 탐색
심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다.
각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.
'''
import sys
input = sys.stdin.readline
def BS(num, s, e, cnt) :
    if s > e : 
        return cnt
    m = (s+e)//2
    if num > B[m] :
        return BS(num, m+1, e, m+1) 
    else : # num <= A[mid]
        return BS(num, s, m-1, cnt) 


T = int(input())
for _ in range(T) :
    a, b = map(int, input().split()) # A, B 생물의 수
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    res = 0
    for num in A :
        res += BS(num, 0, b-1, 0) 
    print(res)

'''
import sys
import bisect
#7795
input = sys.stdin.readline

T = int(input())

for i in range(T):
    sum = 0
    N,M = map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    B.sort()

    for a in A:
        sum += bisect.bisect(B,a-1)
    print(sum)
'''
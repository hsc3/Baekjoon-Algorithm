'''
[10819] 차이를 최대로 | Silver 2 | 백트랙킹
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
'''
import sys
input = sys.stdin.readline

def Calculator(A) :
    global ans
    temp = 0
    for i in range(1, N) :
        temp += abs(A[i] - A[i-1])
    ans = max(ans, temp)

def BT(l) :
    if len(l) == N :
        Calculator(l)
        return
    for idx in range(N) :
        if not v[idx] :
            v[idx] = True
            BT(l+[num[idx]])
            v[idx] = False

if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    v = [False] * N

    ans = 0
    BT([])
    print(ans)
    
'''
import sys
from itertools import permutations
input = sys.stdin.readline

def Calculator(A) :
    global ans
    temp = 0
    for i in range(1, N) :
        temp += abs(A[i] - A[i-1])
    ans = max(ans, temp)

N = int(input())
num = list(map(int, input().split()))
ans = 0
for A in permutations(num, N) :
    Calculator(A)
print(ans)
'''

'''
[15651] N과 M (3) | Silver 3 | 백트랙킹
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 M개를 고른 수열, 같은 수를 여러 번 골라도 된다.
'''
import sys
input = sys.stdin.readline

def Select(choose, cnt) :
    if cnt == m : # m개의 숫자를 모두 고른 경우
        print(' '.join(choose))
        return
    for num in range(1, n+1) :
        Select(choose + str(num), cnt+1) # num을 선택한 경우

if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(1, n+1) :
        Select(str(i), 1)

'''
def Select(choose, i) :
    if i == m : # m개의 숫자를 모두 고른 경우
        print(*choose)
        return
    for num in range(1, n+1) :
        Select(choose + [num], i+1) # num을 선택한 경우

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
Select([], 0)
'''

'''
def dfs(i):
    if len(result) == m : 
        print(str(" ".join(result)))
        return

    for i in range(1, n+1):
        result.append(str(i)) # i 선택
        dfs(i)
        result.pop() # i 선택 x


n, m = map(int, input().split(" "))
result = []
for i in range(1, n+1):
    result.append(str(i))
    dfs(i)
    result.pop()
'''
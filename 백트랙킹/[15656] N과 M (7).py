'''
[15656] N과 M (7) | Silver 3 | 백트랙킹
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. 
- N개의 자연수는 모두 다른 수이다.
- N개의 자연수 중에서 M개를 고른 수열, 같은 수를 여러 번 골라도 된다.
'''
import sys
input = sys.stdin.readline

def Select(choose, cnt) :
    if cnt == m :
        print(*choose)
        return
    for i in range(n) :
        Select(choose + [num[i]], cnt+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    num = sorted(list(map(int, input().split())))
    Select([], 0)
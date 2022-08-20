'''
[15655] N과 M (5) | Silver 3 | 백트랙킹
N개의 자연수와 자연수 M이 주어졌을 때, N개의 자연수 중에서 M개를 고른 수열을 모두 구하는 프로그램을 작성하시오. 
(N개의 자연수는 모두 다른 수이다.)
'''
import sys
input = sys.stdin.readline

def Select(choose, i) :
    if i == m :
        print(*choose)
        return
    for idx in range(n) :
        if visited[idx] == False :
            visited[idx] = True
            Select(choose + [num[idx]], i+1)
            visited[idx] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    visited = [False for _ in range(n)]
    Select([], 0)
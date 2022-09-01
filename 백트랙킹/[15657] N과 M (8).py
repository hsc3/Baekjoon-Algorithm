# [15657] N과 M (8) | Silver 3 | 백트랙킹
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
'''
import sys
input = sys.stdin.readline

def BackTracking(prev, cnt, arr):
    global answer
    if cnt == M:
        answer.append(' '.join(map(str, arr)))
        return
    for i in range(N):
        if prev <= i:
            BackTracking(i, cnt+1, arr + [number[i]])

if __name__ == "__main__":
    N, M = map(int, input().split())
    number = sorted(list(map(int, input().split())))
    answer = []
    BackTracking(-1, 0 , [])
    print(*answer, sep='\n')
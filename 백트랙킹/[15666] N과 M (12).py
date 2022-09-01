# [15666] N과 M (12) | Silver 2 | 백트랙킹
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
'''
import sys
input = sys.stdin.readline

def Backtracking(prev, cnt, arr):
    global answer
    if cnt == M:
        answer.append(arr)
        return

    for i in range(prev, N):
        Backtracking(i, cnt+1, (str(number[i]) if not arr else arr + ' ' + str(number[i])))

if __name__ == "__main__":
    N, M = map(int, input().split())
    number = sorted(list(set(list(map(int, input().split())))))
    N = len(number)

    answer = []
    Backtracking(0, 0, '')
    print(*answer, sep='\n')
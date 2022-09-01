# [15664] N과 M (10) | Silver 2 | 백트랙킹
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 비내림차순이어야 한다.
'''
import sys
input = sys.stdin.readline

def Backtracking(prev_idx, cnt, arr):
    global answer
    if cnt == M:
        answer.append(' '.join(map(str, arr)))
        return
    prev_number = 0 # 이전에 접근한(배열에 들어간) 숫자
    for i in range(prev_idx+1, N):
        if number[i] != prev_number: # 이전에 포함시킨 숫자가 아닌 경우 -> 중복수열 생성 방지
            Backtracking(i, cnt+1, arr + [number[i]])
            prev_number = number[i]

if __name__ == "__main__":
    N, M = map(int, input().split())
    number = sorted(list(map(int, input().split())))
    answer = []
    Backtracking(-1, 0, [])
    print(*answer, sep='\n')
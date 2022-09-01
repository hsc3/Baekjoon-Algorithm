# [15665] N과 M (11) | Silver 2 | 백트랙킹
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
'''
import sys
input = sys.stdin.readline

def Backtracking(cnt, arr):
    global answer
    if cnt == M:
        answer.append(' '.join(map(str, arr)))
        return

    for i in range(N):
        Backtracking(cnt+1, arr + [number[i]])

if __name__ == "__main__":
    N, M = map(int, input().split())
    number = sorted(list(set(list(map(int, input().split()))))) # 중복 숫자 제거
    N = len(number)

    answer = []
    Backtracking(0, [])
    print(*answer, sep='\n')


# def Backtracking(cnt, arr):
#     global answer
#     if cnt == M:
#         answer.append(' '.join(map(str, arr)))
#         return
#
#     prev_num = 0 # 이전에 선택한 숫자 (중복 수열 방지)
#     for i in range(N):
#         if prev_num != number[i]:
#             Backtracking(cnt+1, arr + [number[i]])
#             prev_num = number[i]
#
# if __name__ == "__main__":
#     N, M = map(int, input().split())
#     number = sorted(list(map(int, input().split())))
#
#     answer = []
#     Backtracking(0, [])
#     print(*answer, sep='\n')
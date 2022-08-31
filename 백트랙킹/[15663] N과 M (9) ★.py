# [15663] N과 M (9) | Silver 2 | 백트랙킹
'''
N개의 자연수와 자연수 M이 주어졌을 때, (N개의 자연수 중에서 M개를 고른 수열) 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

# def BackTracking(cnt, arr):
#     global answer, visited
#     if cnt == M:
#         answer.append(' '.join(map(str, arr)))
#         return
#
#     prev_num = 0 # 해당 자리(cnt)에서 이전에 선택한 숫자
#     for i in range(N):
#         if not visited[i] and prev_num != number[i]: # 중복 조합의 경우 제거
#             visited[i] = True
#             prev_num = number[i]
#             BackTracking(cnt+1, arr + [number[i]])
#             visited[i] = False
#
# if __name__ == "__main__":
#     N, M = map(int, input().split())
#     number = sorted(list(map(int, input().split())))
#     visited = [False for _ in range(N)]
#
#     answer = []
#     BackTracking(0, [])
#
#     print(*answer, sep='\n')

def BackTracking(cnt, arr):
    global answer
    if cnt == M:
        arr_to_str = ' '.join(map(str, arr))
        if arr_to_str not in answer:
            answer.add(arr_to_str)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            BackTracking(cnt+1, arr + [number[i]])
            visited[i] = False

if __name__ == "__main__":
    N, M = map(int, input().split())
    number = list(map(int, input().rstrip().split()))
    visited = [False for _ in range(N)]

    answer = set()
    BackTracking(0, [])

    print(*sorted(answer), sep='\n')

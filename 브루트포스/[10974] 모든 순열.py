# [10974] 모든 순열 | Silver 3 | 브루트포스, 백트랙킹
'''
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.
'''
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
for numbers in permutations([i for i in range(1, N+1)], N):
    print(*numbers)

# def Permutation(cnt, number):
#     if cnt == N:
#         answer.append(' '.join(map(str, number)))
#         return
#
#     for i in range(1, N+1):
#         if not visited[i]:
#             visited[i] = True
#             Permutation(cnt+1, number + [i])
#             visited[i] = False
#
#
# if __name__ == "__main__":
#     answer = []
#     N = int(input())
#     visited = [False for _ in range(N+1)]
#     Permutation(0, [])
#     print(*answer, sep='\n')

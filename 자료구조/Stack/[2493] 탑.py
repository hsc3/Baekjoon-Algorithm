# [2493] 탑 | Gold 5 | https://www.acmicpc.net/problem/2493
N = int(input())
tower = list(map(int, input().split()))
stk = []
answer = [0] * N

for i in range(N):
    while stk:
        if stk[-1][1] > tower[i]: # 이전의 타워가 현재의 타워보다 높은 경우
            answer[i] = stk[-1][0] + 1
            break
        else: # 이전의 타워가 더 낮은 경우, 필요 X
            stk.pop()
    stk.append([i, tower[i]])

print(*answer)

# from heapq import heappush, heappop
#
# N = int(input())
# towers = list([height, i+1] for i, height in enumerate(map(int, input().split())))
# answer = [0] * (N+1)
#
# shorter_towers = []
# heappush(shorter_towers, towers.pop())
# while towers:
#     prev_tower = towers.pop()
#     while shorter_towers:
#         if prev_tower[0] >= shorter_towers[0][0]:
#             shorter_tower = heappop(shorter_towers)
#             answer[shorter_tower[1]] = prev_tower[1]
#         else:
#             break
#     heappush(shorter_towers, prev_tower)
#
#
# print(*answer[1:])

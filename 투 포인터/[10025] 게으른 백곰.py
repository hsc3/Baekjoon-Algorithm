# [10025] 게으른 백곰 | Silver 3 | 투 포인터
'''
사육사들이 앨버트의 더위를 식히기 위해 얼음이 담긴 양동이들을 가져다 주었다.
앨버트가 가장 적은 거리만 움직이고도 최대한 많은 얼음으로 더위를 식힐 수 있도록 도와주자.

우리 안은 1차원 배열로 생각하며, 총 N(1 ≤ N ≤ 100000)개의 얼음 양동이들이 Xi(0 ≤ Xi ≤ 1,000,000)좌표마다 놓여 있고
각 양동이 안에는 Gi(1 ≤ Gi ≤ 10,000)씩의 얼음이 들어 있다.
일단 앨버트가 자리를 잡으면 그로부터 좌우로 K(1 ≤ K ≤ 2,000,000) 만큼 떨어진 양동이까지 닿을 수 있다.
앨버트는 양동이가 놓여 있는 자리에도 자리잡을 수 있다. 모든 얼음 양동이의 위치는 다르다.

앨버트가 최적의 자리를 골랐을 때 얼음의 합을 구하시오. 즉, 얼음들의 합의 최댓값을 구해야 한다.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = []
for _ in range(N):
    G, i = map(int, input().split())
    data.append([i, G])
data.sort(key=lambda x:x[0])

left = 0 # X에서 왼쪽 양동이의 인덱스
right = 0 # X에서 오른쪽 양동이의 인덱스
answer = 0

tmp = 0 # 얼음의 양
while right < N:
    left_location = data[left][0] # 왼쪽 양동이의 위치
    right_location = data[right][0] # 오른쪽 양동이의 위치
    if right_location - left_location > 2 * K: # 접근할 수 있는 거리를 넘은 경우 -> 왼쪽 양동이 인덱스 + 1
        tmp -= data[left][1] # tmp -= 왼쪽 양동이 무게
        left += 1
    else: # 접근할 수 있는 거리인 경우 -> 오른쪽 양동이 인덱스 + 1
        tmp += data[right][1] # tmp += 오른쪽 양동이 무게
        answer = max(answer, tmp)
        right += 1

print(answer)

# N, K = map(int, input().split()) # 양동이 갯수, 움직일 수 있는 거리
# X = [0 for _ in range(10000001)] # 양동이 좌표 (value: 얼음의 양)
# left_boundary = float("inf") # 우리의 왼쪽 경계
# right_bounrdary = 0 # 우리의 오른쪽 경계
#
# for _ in range(N):
#     G, i = map(int, input().split())
#     X[i] = G
#     left_boundary = min(left_boundary, i)
#     right_bounrdary = max(right_bounrdary, i)
#
# left = left_boundary
# right = left + (2 * K) + 1
# tmp = sum(X[left:right]) # 좌표 내 얼음의 양
# answer = tmp
# while left <= right_bounrdary - 2*K:
#     tmp -= X[left]
#     left += 1
#     right += 1
#     tmp += X[right]
#     answer = max(answer, tmp)
#
# print(answer)
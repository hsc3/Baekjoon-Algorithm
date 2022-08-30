# [15975] 화살표 그리기 | Silver 3 | 정렬
'''
직선위에 N개의 점들이 주어지고 각 점은 N개의 색깔 중 하나를 가진다. 편의상, 색깔은 1부터 N까지의 수로 표시 하고, 점들의 좌표는 모두 다르다.
각 점 P에 대해서, P에서 시작하는 직선 화살표를 이용해서 다른 점 Q에 연결하려고 한다. 여기서, 점 Q는 P와 같은 색깔의 점들 중 P와 거리가 가장 가까운 점이어야 한다.
만약 가장 가까운 점이 두 개 이상이면 아무거나 하나를 선택한다.

점들의 좌표와 색깔이 주어질 때, 모든 점에서 시작하는 화살표들의 길이 합을 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
data = [[] for _ in range(N+1)] # 색깔 별 점의 위치를 저장
for _ in range(N):
    idx, color = map(int, input().split()) # 점의 위치, 색상
    data[color].append(idx)

# 색깔 별로 점들의 근접한 점까지의 거리를 누적
answer = 0
for i in range(N+1):
    if len(data[i]) > 1: # 같은 색깔의 점이 2개 이상인 경우에만 탐색
        data[i].sort() # 오름차순 정렬
        for j in range(len(data[i])):
            if j == 0: # 가장 왼편의 점인 경우
                answer += (data[i][j+1] - data[i][j])
            elif j == len(data[i])-1: # 가장 오른편의 점인 경우
                answer += (data[i][j] - data[i][j-1])
            else: # 중간에 위치한 점인 경우
                answer += min(data[i][j] - data[i][j-1], data[i][j+1] - data[i][j])

print(answer)

# N = int(input())
# point = sorted([list(map(int, input().split())) for _ in range(N)]) # [점 위치, 색상]
# color = [[] for _ in range(N+1)] # 색깔 기준 점의 위치들 저장
# for point_idx, point_color in point:
#     heappush(color[point_color], point_idx)
#
# answer = 0
# for point_idx, point_color in point:
#     num_of_same_color = len(color[point_color])  # 같은 색상의 점들의 갯수
#     if num_of_same_color == 1: # 같은 색상의 점이 없는 경우
#         continue
#     else:
#         # print("point : ({}, {})".format(point_idx, point_color))
#         idx_in_same_color = color[point_color].index(point_idx) # 같은 색상 내에서 해당 점이 차지하는 위치
#         if idx_in_same_color == 0: # 해당 점이 같은 색상의 점들 중 가장 왼편에 위치한 경우
#             # print("가장 왼편이군요. 거리는 {} 입니다.".format(color[point_color][1] - point_idx))
#             answer += (color[point_color][1] - point_idx)
#         elif idx_in_same_color == num_of_same_color-1: # 해당 점이 같은 색상의 점들 중 가장 오른편에 위치한 경우
#             # print("가장 오른편이군요. 거리는 {} 입니다.".format(point_idx - color[point_color][idx_in_same_color-1]))
#             answer += (point_idx - color[point_color][idx_in_same_color-1])
#         else: # 중간에 위치한 경우
#             # print("중간에 위치했군요. 가장 짧은 거리는 {} 입니다.".format(min((point_idx - color[point_color][idx_in_same_color-1]), (color[point_color][idx_in_same_color+1] - point_idx))))
#             answer += min((point_idx - color[point_color][idx_in_same_color-1]), (color[point_color][idx_in_same_color+1] - point_idx))
#
# print(answer)



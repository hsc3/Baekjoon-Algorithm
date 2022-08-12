# [15970] 화살표 그리기 | Silver 4 | 정렬
'''
직선 위에 위치를 나타내는 0, 1, 2, ...와 같은 음수가 아닌 정수들이 일정한 간격으로 오른쪽 방향으로 놓여 있다. 이러한 위치들 중 N개의 위치에 하나씩 점들이 주어진다.
주어진 점들의 위치는 모두 다르다. 두 점 사이의 거리는 두 점의 위치를 나타내는 수들의 차이이다. 각 점은 N개의 색깔 중 하나를 가진다. 편의상, 색깔은 1부터 N까지의 수로 표시한다.

각 점 p에 대해서, p에서 시작하는 직선 화살표를 이용해서 다른 점 q에 연결하려고 한다. 여기서, 점 q는 p와 같은 색깔의 점들 중 p와 거리가 가장 가까운 점이어야 한다. 만약 가장 가까운 점이 두 개 이상이면 아무거나 하나를 선택한다.
모든 점에 대해서 같은 색깔을 가진 다른 점이 항상 존재한다. 따라서 각 점 p에서 시작하여 위 조건을 만족하는 q로 가는 하나의 화살표를 항상 그릴 수 있다.

점들의 위치와 색깔이 주어질 때, 모든 점에서 시작하는 화살표들의 길이 합을 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
points = dict() # {"색깔" : [해당 색깔의 점들]}
for _ in range(N):
    location, color = map(int,input().split())
    points[color] = points.get(color, []) + [location]

answer = 0
for color in points.keys():
    arr = sorted(points[color]) # 정렬
    for i in range(len(arr)):
        if i == 0: # 가장 왼쪽 점 : 오른쪽 점과의 거리를 구한다.
            answer += (arr[i+1] - arr[i])
        elif i == len(arr) - 1: # 가장 오른쪽 점 : 왼쪽 점과의 거리를 구한다.
            answer += (arr[i] - arr[i-1])
        else: # 중간에 위치한 점들 : 왼쪽과 오른쪽 점 중 가까운 거리를 구한다.
            answer += min(arr[i+1] - arr[i], arr[i] - arr[i-1])

print(answer)
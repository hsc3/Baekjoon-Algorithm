# [18310] 안테나 | Silver 3 | 그리디 알고리즘, 정렬
'''
일직선 상의 마을에 여러 채의 집이 위치해 있다. 이중에서 특정 위치의 집에 특별히 한 개의 안테나를 설치하기로 결정했다. 효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치하려고 한다.
이 때 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 선택하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
house_locations = sorted(list(map(int, input().split()))) # 집의 위치
center_first = (N-1) // 2 # 집들의 가운데에 위치하는 집 중 왼쪽 집의 위치
print(house_locations[center_first])


# if N == 1:
#     print(house_locations[0])
# elif N % 2 == 0:
#     house_at_centers = house_locations[N // 2 - 1 : N // 2 + 1]
#     center = sum(house_at_centers) // 2
#     locations_from_center = sorted([[abs(center-location), location] for location in house_at_centers])
#     print(locations_from_center[0][1])
# else:
#     print(house_locations[N//2])

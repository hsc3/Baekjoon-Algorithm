# [2110] 공유기 설치 | Gold 4 | 이분 탐색
'''
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에,
한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def CheckDistance(distance): # 현재 집과 다음 집의 거리를 계산한다.
    cnt = 1 # 공유기 설치 대수
    curr = 0 # 현재 집의 좌표
    next = 1 # 다음 집의 좌표
    while cnt < C and next < N: # 아직 C개의 공유기를 설치하지 않았고, 마지막 집까지 거리 계산을 하지 않은 경우에 탐색을 지속
        if X[next] - X[curr] >= distance: # 두 집 사이의 거리가 distance 이상인 경우 -> 공유기를 설치하고 다음 집을 기준으로 거리 계산
            cnt += 1
            curr = next
            next += 1
        else: # 두 집 사이의 거리가 distance 미만인 경우 -> 현재 집을 next + 1 위치의 집과 거리 계산
            next += 1

    return cnt >= C

if __name__ == "__main__":
    N, C = map(int, input().split())
    X = sorted(list(int(input()) for _ in range(N)))

    answer = 0
    left, right = 1, X[-1] - X[0]

    while left <= right: # 두 집 사이의 거리를 기준으로 이분 탐색 수행
        mid = (left + right) // 2 
        if CheckDistance(mid): # 공유기를 설치할 수 있는 경우, 거리를 더 늘린다.
            left = mid + 1
            answer = mid
        else: # 공유기를 설치할 수 없는 경우, 거리를 줄인다.
            right = mid - 1

print(answer)
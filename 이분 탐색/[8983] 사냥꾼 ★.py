# [8983] 사냥꾼 | Gold 4 | https://www.acmicpc.net/problem/8983
import sys
input = sys.stdin.readline

# 동물의 x 좌표를 기준으로 가장 근접한 사대를 탐색한다.
# 동일 선상의 사대가 존재하는 경우 -> 동물과 사대의 사이의 거리가 사정 거리 내 인지 비교
# 동일 선상의 사대가 존재하지 않는 경우 -> 가장 근접한 두 사대를 탐색해서, 두 사대의 사정 거리 내 인지 비교

answer = 0 # 잡을 수 있는 동물의 수

M, N, L = map(int, input().split()) # 사대, 동물, 사정거리
X = sorted(list(map(int, input().split()))) # 사대 위치 (오름차순 정렬)
animal = [list(map(int, input().split())) for _ in range(N)] # 동물의 위치

for a_x, a_y in animal:
    start = 0
    end = M-1
    # print("동물의 위치 = [{}, {}]".format(a_x, a_y))
    checked = False
    while start < end: # 사대의 인덱스를 기준으로 이분 탐색
        mid = (start + end) // 2
        if X[mid] == a_x: # 사대와 동물이 동일한 x 좌표에 위치한 경우 -> 가장 가까운 사대
            # print("- 동일 선상의 사대(Xi={})를 선택했습니다.".format(X[mid]))
            checked = True
            if abs(X[mid] - a_x) + a_y <= L:
                # print("- 해당 사대의 사정 거리 안에 동물이 들어옵니다.")
                answer += 1
            # else:
                # print("- 해당 사대의 사정 거리 안에 동물이 들어오지 않습니다.")
            break
        elif X[mid] < a_x: # 사대의 x 좌표 < 동물의 x 좌표 -> 오른쪽 사대를 선택
            start = mid + 1
            # print("- 사대(Xi={})보다 오른쪽 사대를 선택해야 합니다.".format(X[mid]))
        else: # 사대의 x 좌표 < 동물의 x 좌표 -> 왼쪽 사대를 선택
            # print("- 사대(Xi={})보다 왼쪽 사대를 선택해야 합니다.".format(X[mid]))
            end = mid
    if not checked:
        # print("- 가장 근접한 사대(Xi={}, {})를 선택했습니다.".format(X[end-1], X[end]))
        if abs(X[end] - a_x) + a_y <= L or abs(X[end-1] - a_x) + a_y <= L:  # 동물이 사정거리 안에 있는 경우
            # print("- 두 사대의 사정 거리 안에 동물이 들어왔습니다.")
            answer += 1
        # else:
        #     print("- 두 사대의 사정 거리 안에 동물이 들어오지 않습니다.")
    # print()

print(answer)
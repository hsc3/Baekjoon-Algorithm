# [2792] 보석 상자 | Silver 2 | 이분 탐색
'''
보석 공장에서 보석 상자를 유치원에 기증했다. 각각의 보석은 M가지 서로 다른 색상 중 한 색상이다. 원장 선생님은 모든 보석을 N명의 학생들에게 나누어 주려고 한다.
이때, 보석을 받지 못하는 학생이 있어도 된다. 하지만, 학생은 항상 같은 색상의 보석만 가져간다.
한 아이가 너무 많은 보석을 가져가게 되면, 다른 아이들이 질투를 한다. 원장 선생님은 이런 질투심을 수치화하는데 성공했는데, 질투심은 가장 많은 보석을 가져간 학생이 가지고 있는 보석의 개수이다.
원장 선생님은 질투심이 최소가 되게 보석을 나누어 주려고 한다.
상자 안의 보석 정보와 학생의 수가 주어졌을 때, 질투심이 최소가 되게 보석을 나누어주는 방법을 알아내는 프로그램을 작성하시오.
'''
import math
import sys
input = sys.stdin.readline

def GiveJewelry(mid): # 최대 mid개만큼 보석을 나눠줬을 때, 보석이 남지 않는지를 판별.
    cnt = 0
    for c in color:
        cnt += math.ceil(c / mid)

    return (cnt <= N)
    # return True if cnt <= N else False

if __name__ == "__main__":
    N, M = map(int, input().split()) # 아이들, 색상의 수
    color = list(int(input()) for _ in range(M))

    answer = float("inf")
    left, right = 1, max(color)
    while left <= right: # 보석의 갯수를 기준으로 이분 탐색을 수행한다.
        mid = (left + right) // 2

        if GiveJewelry(mid): # mid개 나눠줬을 때, 보석이 남지 않는 경우
            answer = min(answer, mid) # 최소 질투심( = 최대 보석 갯수 : mid)을 갱신한다.
            right = mid - 1 # 더 조금 나눠주는 경우를 탐색
        else:
            left = mid + 1 # 더 많이 나눠주는 경우를 탐색

print(answer)

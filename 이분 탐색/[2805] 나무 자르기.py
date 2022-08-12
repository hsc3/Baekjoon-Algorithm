# [2805] 나무 자르기 | Silver 2 | 이분 탐색
'''
Q : 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
'''
import sys 
input = sys.stdin.readline
def CuttheTrees(trees, h) :
    h_sum = 0
    for tree in trees :
        if tree - h > 0 :
            h_sum += (tree - h)
    return h_sum

N, M = map(int, input().split()) # N : 나무의 갯수,  M : 필요한 나무의 길이
trees = list(map(int, input().split()))
# 자를 나무의 높이
h_max = max(trees) 
h_min = 0
# 가장 적게 잘라가야 함.
while h_min <= h_max :
    h_mid = (h_max + h_min) // 2
    if CuttheTrees(trees, h_mid) >= M : # 필요한 나무 길이를 만족하는 경우 -> 더 조금 잘라본다
        h_min = h_mid + 1
    else : # 더 많이 잘라야 한다.
        h_max = h_mid - 1
print(h_max)

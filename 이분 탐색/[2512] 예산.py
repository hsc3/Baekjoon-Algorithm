# [2512] 예산 | Silver 3 | 이분 탐색
'''
Q : 정해진 총액 이하에서 가능한 한 최대의 총 예산을 배정하자.
1. 모든 요청이 배정될 수 있는 경우, 요청한 금액을 그대로 배정한다.
2. 모든 요청이 배정될 수 없는 경우, 특정한 정수 상한액을 계산하여 그 이상인 예산 요청에는 모두 상한액을 배정한다.
출력 : 배정된 예산들 중 최대값을 출력하라.
'''
import sys
input = sys.stdin.readline
def Calculator(request, max_budget, full_budget) : # 예산 계산기
    sum = 0 
    for budget in request :
        if budget <= max_budget :
            sum += budget 
        else :    
            sum += max_budget
    if sum <= full_budget : return 1 
    else : return 0

N = int(input()) # 지방의 수
request = list(map(int, input().split()))
M = int(input()) # 총 예산
if sum(request) <= M : print(max(request))
else :
    start = M // N - 1 # 각 지방에 줄 수 있는 최소 예산
    end = max(request) + 1 # 각 지방에 줄 수 있는 최대 예산
    mid = (start + end) // 2

    while mid != start and mid != end :
        if Calculator(request, mid, M) == 1 : 
            start = mid
        else : 
            end = mid
        mid = (start + end) // 2
    print(mid)
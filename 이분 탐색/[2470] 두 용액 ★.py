# [2470] 두 용액 | Gold 5 | 이분 탐색
'''
<< Binary Search 이분탐색 >>
Q : 두 용액을 합쳐 가장 농도가 0에 가까운 용액을 만드시오.
- 첫째 줄에는 전체 용액의 수 N이 입력된다. 
  둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 
  N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.
- 첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다. 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다. 
'''

'''
import sys
sys.setrecursionlimit(10**6)

def BSearch(arr, min_idx, max_idx, min_num, max_num, nongdo) :

    if min_idx == max_idx :
        return min_num, max_num

    else :
        al = arr[min_idx] # 가장 산성이 낮은 용액
        san = arr[max_idx] # 가장 산성이 높은 용액

        new_nongdo = abs(al + san)
        if nongdo > new_nongdo : 
            nongdo = new_nongdo
            min_num = al
            max_num = san

        if al + san < 0 : # 산성이 더 높은 용액을 선택 
            return BSearch(arr, min_idx + 1, max_idx, min_num, max_num, nongdo)
        elif al + san > 0 : # 알칼리성이 더 높은 용액을 선택
            return BSearch(arr, min_idx, max_idx - 1, min_num, max_num, nongdo)
        else :
            return min_num, max_num
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(*BSearch(arr, 0, N - 1, 0, 0, float("inf")))
'''

import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = n-1
answer = liquid[left] + liquid[right]
idxl = left
idxr = right
while left < right:
    tmp = liquid[left] + liquid[right]
    if abs(tmp) < abs(answer):
        answer = tmp
        idxl = left
        idxr = right
        if answer == 0:
            break
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(liquid[idxl], liquid[idxr])

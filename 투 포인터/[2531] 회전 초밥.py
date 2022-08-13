# [2531] 회전 초밥 | Silver 1 | 투 포인터
'''
회전 초밥 음식점에는 회전하는 벨트 위에 여러 가지 종류의 초밥이 접시에 담겨 놓여 있고, 손님은 이 중에서 자기가 좋아하는 초밥을 골라서 먹는다. 벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다.
새로 문을 연 회전 초밥 음식점이 불경기로 영업이 어려워서, 다음과 같이 두 가지 행사를 통해서 매상을 올리고자 한다.
1. 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공한다.
2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공한다. 만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공한다.

회전 초밥 음식점의 벨트 상태, 메뉴에 있는 초밥의 가짓수, 연속해서 먹는 접시의 개수, 쿠폰 번호가 주어졌을 때, 손님이 먹을 수 있는 초밥 가짓수의 최댓값을 구하는 프로그램을 작성하시오.
* 최대값 -> 쿠폰 번호의 초밥이 포함되지 않은 지점의 초밥을 연속으로 먹어야 한다.
'''
import sys
from collections import Counter
input = sys.stdin.readline

# 시간 : 144ms
N, D, K, C = map(int, input().split()) # 접시 수, 초밥의 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
sushi = [int(input()) for _ in range(N)]
sushi += sushi[:K-1]
start = 0
end = K

answer = [] # 초밥의 가짓수
eat = Counter(sushi[start:end]) # K개의 연속된 초밥들

while start < N-1: # 시계 방향으로 1칸씩 이동
    answer.append(len(eat.keys()) + (1 if C not in eat.keys() else 0)) # 쿠폰 번호의 초밥을 1개 추가한 가짓수 저장
    eat[sushi[end]] += 1 # 오른쪽 초밥 추가
    eat[sushi[start]] -= 1 # 왼쪽 초밥 제거
    if eat[sushi[start]] == 0:
        eat.pop(sushi[start])
    
    start += 1
    end += 1

print(max(answer))

''' 시간 : 3240ms
import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split()) # 접시 수, 초밥의 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
sushi = [int(input()) for _ in range(N)]
sushi += sushi[:K-1]
start = 0
end = K

answer = [] # 초밥의 가짓수
while start < N-1: # 시계 방향으로 1칸씩 이동
    eat = set(sushi[start:end] + [C]) # (K개의 연속된 초밥 + 쿠폰 번호의 초밥)의 가짓수
    answer.append(len(eat))
    start += 1
    end += 1

print(max(answer))
'''
# [2018] 수들의 합 5 | Silver 5 | 투 포인터
'''
어떠한 자연수 N은, 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 당신은 어떤 자연수 N(1 ≤ N ≤ 10,000,000)에 대해서, 이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지 수를 알고 싶어한다.
이때, 사용하는 자연수는 N 이하여야 한다. 예를 들어, 15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다. 반면에 10을 나타내는 방법은 10, 1+2+3+4의 2가지가 있다.

N을 입력받아 가지수를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())

left, right = 1, 1
sumOfNum = left
answer = 1 if N//2 + 2 <= N else 0

''' 슬라이딩 윈도우ㅈ
1    2    3    4    5    6    7    8
|-------------------|
               |---------|
                              |----|
'''

while True:
    if right == N//2 + 2:
        break
    if sumOfNum == N: # 슬라이딩 윈도우를 오른쪽을 한 칸 이동
        answer += 1
        sumOfNum -= left
        left += 1
        right += 1
        sumOfNum += right
    elif sumOfNum > N: # 슬라이딩 윈도우의 왼쪽을 1칸 축소
        sumOfNum -= left
        left += 1
    else: # sumOfNum < N 슬라이딩 윈도우의 오른쪽을 1칸 확장
        right += 1
        sumOfNum += right

print(answer)
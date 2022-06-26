'''
[2003] 수들의 합 (2) / Silver 4 / 투 포인터
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 10, 5
numbers = list(map(int, input().split()))

res = 0

leftCursor, rightCursor = 0, 0
sumOfArr = sum(numbers[leftCursor : rightCursor + 1]) # 전체 배열의 덧셈 연산 중복 제거 (하나의 원소만 증감시킨다.)

while True :
    if sumOfArr == M : # 숫자의 합이 M과 같은 경우, 왼쪽 숫자와 오른쪽 숫자의 index + 1 (슬라이딩 윈도우)
        res += 1
        sumOfArr -= numbers[leftCursor]
        leftCursor += 1
        rightCursor += 1
        if rightCursor == N : break
        sumOfArr += numbers[rightCursor]
    
    elif sumOfArr > M : # 숫자의 합이 M보다 큰 경우, 왼쪽 숫자의 index + 1
        sumOfArr -= numbers[leftCursor]
        leftCursor += 1
    
    else : # 숫자의 합이 M보다 작은 경우, 오른쪽 슷자의 index + 1
        rightCursor += 1
        if rightCursor == N : break
        sumOfArr += numbers[rightCursor]

print(res)

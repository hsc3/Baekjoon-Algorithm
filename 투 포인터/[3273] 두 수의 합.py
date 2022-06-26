'''
[3273] 두 수의 합 / Silver 3 / 투 포인터, 정렬
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다.
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split()))) # [1, 2, 3, 5, 7, 9, 10, 11, 12]
x = int(input())

res = 0

leftCursor = 0 # 배열의 왼편 숫자의 위치
rightCursor = n-1 # 배열의 오른편 숫자의 위치

while leftCursor < rightCursor :
    if arr[leftCursor] + arr[rightCursor] == x : # 두 수의 합이 x와 같은 경우
        res += 1
        leftCursor += 1 # 배열의 다음 숫자들을 체크
        rightCursor -= 1
    elif arr[leftCursor] + arr[rightCursor] > x : # 두 수의 합이 x보다 큰 경우
        rightCursor -= 1 # 배열의 가장 오른쪽 숫자 배제(왼쪽의 어떤 숫자와 더해도 x보다 큰 값이 된다.)
    else : # x보다 작은 경우
        leftCursor += 1 # 배열의 가장 왼쪽 숫자 배제

print(res)

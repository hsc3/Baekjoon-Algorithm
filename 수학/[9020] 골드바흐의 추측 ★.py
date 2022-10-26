# [9020] 골드바흐의 추측 | Silver 2 | https://www.acmicpc.net/problem/9020
import sys
input = sys.stdin.readline
from math import sqrt

# 정수론, 소수 판별
def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    answer = []

    for _ in range(int(input())):
        n = int(input())
        mid = n // 2
        if isPrime(mid):
            answer.append([mid, mid])
        else:
            if mid % 2 == 0: # n=16인 경우, mid=8은 소수가 아니므로, (7+9), (5+11), ...의 규칙으로 파티션을 찾아나간다.
                i = 1
            else: # n=18인 경우, mid=9는 소수가 아니므로, (7+11), (5+13), ...의 규칙으로 파티션을 찾아나간다.
                i = 2

            while True:
                if isPrime(mid-i) and isPrime(mid+i):
                    answer.append([mid-i, mid+i])
                    break
                i += 2

    for a in answer:
        print(*a)


# # 에라토스테네스의 체 (n 미만의 소수 판별) -> 투 포인터로 차이가 가장 작은 골드바흐 파티션 찾기
# def findPrime(n):
#
#     checked = [False for _ in range(n)]
#
#     for i in range(2, int(sqrt(n))+1):
#         if not checked[i]: # i는 소수
#             for num in range(2*i, n, i):
#                 checked[num] = True # i의 배수는 소수x
#
#     allPrime = []
#     for i in range(2, n):
#         if not checked[i]:
#             allPrime.append(i)
#
#     return allPrime # n 미만의 소수들 반환
#
#
# def findPartition(left, right):
#     global biggest_left, smallest_right
#     if left > right:
#         return
#
#     if primeNums[left] + primeNums[right] > n: # 두 소수의 합이 n보다 큰 경우 -> 더 작은 소수를 선택
#         findPartition(left, right-1)
#     elif primeNums[left] + primeNums[right] < n: # 두 소수의 합이 n보다 작은 경우 -> 더 큰 소수를 선택
#         findPartition(left+1, right)
#     else: # 두 소수의 합이 n과 같은 경우 -> 골드바흐 파티션 o
#         biggest_left = primeNums[left]
#         smallest_right = primeNums[right]
#         findPartition(left+1, right-1)
#
#
#
# if __name__ == "__main__":
#     answer = []
#
#     for _ in range(int(input())):
#         n = int(input())
#         primeNums = findPrime(n)
#         biggest_left, smallest_right = 0, 0
#         findPartition(0, len(primeNums)-1)
#         answer.append([biggest_left, smallest_right])
#
#     for a in answer:
#         print(*a)
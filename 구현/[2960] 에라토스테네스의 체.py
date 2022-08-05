# [2960] 에라토스테네스의 체 | Silver 4 | 구현
'''
에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다. 이 알고리즘은 다음과 같다.
1. 2부터 N까지 모든 정수를 적는다.
2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
erase = [False] * (N+1)

prime = []
# 앞선 소수의 배수들을 지우기 때문에 결국 소수만 남게 된다. 따라서 소수인지를 판별할 필요가 없다.
for num in range(2, N+1):
    for multipleNum in range(num, N+1, num): # num의 배수
        if not erase[multipleNum]:
            erase[multipleNum] = True
            prime.append(multipleNum)

print(prime[K-1])


# def isPrimeNumber(number): # 소수 판별 함수
#     for i in range(2, number):
#         if number % i == 0:
#             return False # 소수 X
#     return True # 소수 O
#
# def program(N, K):
#     cnt = 0
#     for number in range(2, N+1):
#         if isPrimeNumber(number): # number가 소수인 경우
#             for i in range(1, N//number+1):
#                 multipleNumber = number * i # number의 배수
#                 if not erase[multipleNumber]: # 아직 지우지 않은 경우,  number의 배수를 지운다
#                     erase[multipleNumber] = True
#                     cnt += 1
#                     if cnt == K:
#                         return number * i
#
# if __name__ == "__main__":
#     N, K = map(int, input().split())
#     erase = [False]*(N+1)
#     answer = program(N, K)
#     print(answer)

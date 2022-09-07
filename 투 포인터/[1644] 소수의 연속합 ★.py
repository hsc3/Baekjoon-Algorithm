# [1644] 소수의 연속합 | Gold 3 | 투 포인터
'''
하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.
3 : 3 (한 가지)
41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
53 : 5+7+11+13+17 = 53 (두 가지)
하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다.
또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.
자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.
'''
from math import sqrt

N = int(input())
prime = [True for _ in range(N+1)]# 0 ~ N까지의 숫자가 소수인지 여부
# [1] N까지의 소수 판별
for num in range(2, int(sqrt(N))+1):
    if prime[num]:
        for multiple_num in range(num*2, N+1, num): # 소수의 배수들은 모두 소수가 아니다.
            prime[multiple_num] = False

prime_number = []
for num in range(2, N+1):
    if prime[num]:
        prime_number.append(num)

# [2] 연속된 소수 합 판별
left, right = 0, 1
sum_of_prime_numbers = sum(prime_number[left:right])
answer = (1 if N in prime_number else 0) # 자기 자신이 소수인지 체크

while right < len(prime_number):
    if sum_of_prime_numbers <= N: # 소수들의 연속된 합이 N 이하인 경우 -> right + 1
        if sum_of_prime_numbers == N:
            answer += 1
        sum_of_prime_numbers += prime_number[right]
        right += 1

    else: # 소수들의 연속된 합이 N보다 큰 경우 -> left + 1
        sum_of_prime_numbers -= prime_number[left]
        left += 1

print(answer)


# [4948] 베르트랑 공준 | Silver 3 | https://www.acmicpc.net/problem/4948
from math import sqrt

def FindPrimeNumbers(n): # n ~ 2n
    for i in range(2, int(sqrt(n))+1):
        if not checked[i]: # i = 소수
            for num in range(2*i, n+1, i):
                checked[num] = True # num = 소수의 배수 (소수 x)

numbers = []
while True:
    number = int(input())
    if number == 0:
        break
    numbers.append(number)

max_n = 2 * max(numbers)
checked = [True, True] + [False for _ in range(max_n-1)]
FindPrimeNumbers(max_n) # 입력받은 숫자들 중, 가장 큰 숫자를 기준으로 모든 소수를 구한다.

for number in numbers:
    print(checked[number+1:(2*number)+1].count(False)) # n보다 크고, 2n보다 작거나 같은 소수의 개수
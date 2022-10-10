# [1676] 팩토리얼 0의 개수 | Silver 5 | https://www.acmicpc.net/problem/1676
from math import factorial

answer = 0
num = str(factorial(int(input())))[::-1]
for i in range(len(num)):
    if num[i] != '0':
        answer = i
        break

print(answer)
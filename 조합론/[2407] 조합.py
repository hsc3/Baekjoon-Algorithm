# [2407] 조합 | Silver 4 | 조합론
'''
nCm을 출력하는 프로그램을 작성하라.
'''
from math import factorial

n, m = map(int, input().split())
if m > n - m: # (ex) 6C4 -> 6C2
    m = n - m

# 분자와 분모 계산
numerator = 1 # 분자
denominator = factorial(m) # 분모
for i in range(m):
    numerator *= (n-i)
    
print(numerator // denominator)

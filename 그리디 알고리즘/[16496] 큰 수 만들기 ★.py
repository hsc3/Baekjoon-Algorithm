# [16496] 큰 수 만들기 / Platinum 5 /  그리디, 정렬
'''
음이 아닌 정수(0보다 크거나 같은 정수)가 N개 들어있는 리스트가 주어졌을 때,
리스트에 포함된 수를 나열하여 만들 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
'''
import sys 
from functools import cmp_to_key
input = sys.stdin.readline

N = int(input()) # 수의 갯수
numbers = list(input().split())
# 숫자를 문자열 형태로 a + b 와 b + a의 형태로 합쳐보고 큰 것을 기준으로 정렬한다.
# 3 30 34 5 9 -> 9534330
# 9 95 6 62 4 -> 9956624
numbers.sort(key = cmp_to_key(lambda a, b : 1 if int(a+b) < int(b+a) else -1))
    
print(int(''.join(numbers)))
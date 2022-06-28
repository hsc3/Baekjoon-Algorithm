'''
[11720] 숫자의 합 / Bronze 4 / 문자열
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

N = int(input()) # 숫자의 개수
numbers = list(map(int, input().rstrip()))
print(sum(numbers))

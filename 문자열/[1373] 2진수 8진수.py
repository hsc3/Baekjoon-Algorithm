'''
[1373] 2진수 8진수 / Bronze 1 / 문자열, 수학
2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline
from collections import deque

binary = list(map(int, input().rstrip())) # 11001100
octal = deque()

squareNum = 0 
tmp = 0

for num in binary[::-1] :
    if squareNum > 2 : # 2진수의 3비트 단위로 끊어 합산 (8진수로 변환)
        squareNum = 0
        octal.appendleft(tmp)
        tmp = 0

    tmp += (num*(2**squareNum))
    squareNum += 1

octal.appendleft(tmp)

print(*octal, sep='')

'''
A = int(input(), 2) # 입력받을 때 2진수로 입력을 받고
print(oct(A)[2:]) # 출력할 때 8진수로 출력한다.
'''

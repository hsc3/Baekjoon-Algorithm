'''
* 구현, 문자열
[10820] 문자열 분석 | https://www.acmicpc.net/problem/10820
문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

while True :

    string = input().rstrip('\n')
    if not string :
        break

    lower = 0
    upper = 0
    numeric = 0
    space = 0
        
    for c in string :
        if c.islower() :
            lower += 1
        elif c.isupper() :
            upper += 1
        elif c.isnumeric() :
            numeric += 1
        else :
            space += 1
    print(lower, upper, numeric, space)
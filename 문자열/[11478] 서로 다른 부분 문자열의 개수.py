# [11478] 서로 다른 부분 문자열의 개수 / Silver 3 / 문자열, 자료구조(Set)
# 문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

import sys ; input = sys.stdin.readline

res = []
S = input().rstrip() # "ababc"

for i in range(len(S)) :
    for j in range(1, len(S)-(i-1)) : 
        res.append(S[i : i+j]) 

print(len(set(res)))

# set 자료형에 add 하는 것보단, list 자료형에 append하고 최종적으로 set 자료형으로 바꾸는 것이 더 빠름.
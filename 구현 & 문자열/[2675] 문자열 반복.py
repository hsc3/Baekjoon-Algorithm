# [2675] 문자열 반복
# Bronze 2 >> 구현, 문자열

import sys
input = sys.stdin.readline

res = []
for _ in range(int(input())) :
    time, string = input().split()
    res.append(''.join([s * int(time) for s in string]))

print(*res, sep = '\n')
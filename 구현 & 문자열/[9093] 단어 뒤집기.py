# [9093] 단어 뒤집기
# Bronze 1 >> 문자열
# 문자이 주어졌을 때, 모든 단어를 뒤집어서 출력하는 프로그램을 작성하시오
import sys
input = sys.stdin.readline

res = []

for _ in range(int(input())) :
    reversedString = [s[::-1] for s in list(input().split())]
    res.append(reversedString)

for r in res :
    print(*r, sep = ' ')
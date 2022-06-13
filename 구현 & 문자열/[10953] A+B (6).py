# 문자열 [10953] A+B (6) | https://www.acmicpc.net/problem/10953
import sys
input = sys.stdin.readline

answer = []
for i in range(int(input())) :
    numbers = list(map(int, input().split(',')))
    answer.append(sum(numbers))

print(*answer, sep='\n')
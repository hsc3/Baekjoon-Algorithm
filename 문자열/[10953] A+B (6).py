# [10953] A+B (6) / Bronze 2 / 문자열, 파싱
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

answer = []
for i in range(int(input())) :
    numbers = list(map(int, input().split(',')))
    answer.append(sum(numbers))

print(*answer, sep='\n')
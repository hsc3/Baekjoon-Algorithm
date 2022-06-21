'''
[2751] 수 정렬하기 (2) / Silver 5 / 정렬
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

numbers = set(int(input()) for _ in range(int(input())))
print(*sorted(numbers), sep = '\n')

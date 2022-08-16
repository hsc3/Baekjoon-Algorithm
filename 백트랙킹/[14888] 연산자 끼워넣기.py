# [14888] 연산자 끼워넣기 | Silver 1 | 백트랙킹, 브루트포스
'''
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

# 백트랙킹 풀이
def Calculator(i, total, plus, minus, multiply, divide):
    global maximum, minimum

    if i == N: # 최대, 최소값 저장
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return

    if plus: # 덧셈
        Calculator(i+1, total + operand[i], plus-1, minus, multiply, divide)
    if minus: # 뺄셈
        Calculator(i+1, total - operand[i], plus, minus-1, multiply, divide)
    if multiply: # 곱셈
        Calculator(i+1, total * operand[i], plus, minus, multiply-1, divide)
    if divide: # 나눗셈
        Calculator(i+1, int(total / operand[i]), plus, minus, multiply, divide-1)

if __name__ == "__main__":

    N = int(input())
    operand = list(map(int, input().split()))
    operation = list(map(int, input().split()))

    maximum = -float("inf")
    minimum = float("inf")
    Calculator(1, operand[0], operation[0], operation[1], operation[2], operation[3])

    print(maximum)
    print(minimum)

# 브루트포스 풀이
# import sys
# from itertools import permutations
# input = sys.stdin.readline
#
# N = int(input())
# operand = list(map(int, input().split()))
# operation_cnt = list(map(int, input().split())) # 0:+, 1:-, 2:x, 3:%
# operations = []
# for op in range(4):
#     for _ in range(operation_cnt[op]):
#         operations.append(op)
# operations = list(permutations(operations, N-1)) # 연산자의 조합 가능한 모든 경우
#
# maxAnswer = -float("inf")
# minAnswer = float("inf")
# for operation in operations:
#     tmp = operand[0]
#     for i in range(N-1):
#         if operation[i] == 0: # 덧셈
#             tmp += operand[i+1]
#         elif operation[i] == 1: # 뺄셈
#             tmp -= operand[i+1]
#         elif operation[i] == 2: # 곱셈
#             tmp *= operand[i+1]
#         else: # 나눗셈
#             tmp = int(tmp / operand[i+1])
#     maxAnswer = max(maxAnswer, tmp)
#     minAnswer = min(minAnswer, tmp)
#
# print(maxAnswer)
# print(minAnswer)
# [15658] 연산자 끼워넣기 (2) | Silver 2 | 백트랙킹
'''
개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 연산자가 주어진다.
연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다. 연산자의 개수는 N-1보다 많을 수도 있다.
우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다.
음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
N개의 수와 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def BackTracking(result, i, op1, op2, op3, op4):
    if i == N:
        answer.append(result)
        return

    if op1 != 0: # + 연산
        BackTracking(result+num[i], i+1, op1-1, op2, op3, op4)
    if op2 != 0: # - 연산
        BackTracking(result-num[i], i+1, op1, op2-1, op3, op4)
    if op3 != 0: # * 연산
        BackTracking(result*num[i], i+1, op1, op2, op3-1, op4)
    if op4 != 0: # / 연산
        BackTracking(int(result/num[i]), i+1, op1, op2, op3, op4-1)

if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    op = list(map(int, input().split()))

    answer = []
    BackTracking(num[0], 1, op[0], op[1], op[2], op[3])

    print(max(answer))
    print(min(answer))
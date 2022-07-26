# [1935] 후위 표기식 2 | Silver 3 | 자료구조(stack)
'''
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def Calculator(n1, n2, op) :
    if op == '*' :   return n1 * n2
    elif op == '+' : return n1 + n2
    elif op == '-' : return n1 - n2
    else : return n1 / n2

if __name__ == "__main__" :
    N = int(input()) # 피연산자의 갯수
    rear_notation = list(input().rstrip()) # 후위 표기식
    num = [int(input()) for _ in range(N)] # 피연산자 
    
    stk = []
    for c in rear_notation :
        if c.isalpha() :
            stk.append(num[ord(c) - 65])
        else : # 사칙연산
            n2 = stk.pop()
            n1 = stk.pop()
            stk.append(Calculator(n1, n2, c))

    print("{:.2f}".format(stk.pop()))
    # print('%.2f'%stk.pop)
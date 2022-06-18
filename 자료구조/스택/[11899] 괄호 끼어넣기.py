'''
[11899] 괄호 끼어넣기 / Silver 3 / 자료구조(스택)
망가뜨리고 사용 가능한 올바르지 않은 괄호열이 주어질 때, 올바른 괄호열으로 만들기 위해 
앞과 뒤에 붙여야 할 괄호의 최소 개수를 구하는 프로그램을 작성하세요.
'''
import sys
input = sys.stdin.readline

brokenBracket = list(input().rstrip())
stk = []
res = 0

for i in range(len(brokenBracket)) :
    if brokenBracket[i] == '(' :
        stk.append(brokenBracket[i]) # 여는 괄호는 스택에 넣는다.
    else : # 닫는 괄호일 경우
        if stk : # 스택에 쌍을 이루는 여는 괄호가 있을 경우, 스택에서 하나를 제거한다.
            stk.pop()
        else : # 스택에 여는 괄호가 없을 경우, 여는 괄호 1개를 추가한다.
            res += 1

print(res + len(stk)) # len(stk) : 추가하는 닫는 괄호의 개수
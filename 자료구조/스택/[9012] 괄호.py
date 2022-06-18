'''
[9012] 괄호 / Silver 4 / 자료구조(스택)
입력으로 주어진 괄호 문자열이 올바른 괄호 문자열인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

res = []

for _ in range(int(input())) :
    bracketString = list(input().rstrip())
    stk = []
    breakFlag = False

    for i in range(len(bracketString)) :
        if bracketString[i] == '(' : # 여는 괄호는 스택에 넣는다.
            stk.append(bracketString[i])
        else : # 닫는 괄호일 경우
            if stk : # 여는 괄호가 있으면, 스택에서 하나를 제거
                stk.pop()
            else : # 여는 괄호가 없으면, 올바른 괄호 문자열X
                breakFlag = True
                break
    
    if breakFlag or len(stk) > 0 : 
        res.append("NO")
    else :
        res.append("YES")

print(*res, sep = '\n')
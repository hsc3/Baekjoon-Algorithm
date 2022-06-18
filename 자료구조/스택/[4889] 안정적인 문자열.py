'''
[4889] 안정적인 문자열 / Silver 1 / 자료구조(스택), 그리디 알고리즘
여는 괄호와 닫는 괄호만으로 이루어진 문자열이 주어진다. 여기서 안정적인 문자열을 만들기 위한 최소 연산의 수를 구하려고 한다. 
안정적인 문자열의 정의란 다음과 같다.
1. 빈 문자열은 안정적이다.
2. S가 안정적이라면, {S}도 안정적인 문자열이다.
3. S와 T가 안정적이라면, ST(두 문자열의 연결)도 안정적이다.
문자열에 행할 수 있는 연산은 여는 괄호를 닫는 괄호로 바꾸거나, 닫는 괄호를 여는 괄호로 바꾸는 것 2가지이다.
각 테스트 케이스에 대해서, 테스트 케이스 번호와 입력으로 주어진 문자열을 안정적으로 바꾸는데 필요한 최소 연산의 수를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
res = []

while True :
    inputString = list(input().rstrip())
    
    if '-' in inputString :
        break

    stk = []
    change = 0
    
    for i in range(len(inputString)) :
        if inputString[i] == '}' :
            if stk : # 닫는 괄호에 매치되는 여는 괄호가 있는 경우
                stk.pop()
            else : # 여는 괄호가 없는 경우, 닫는 괄호를 여는 괄호로 변경하고 스택에 넣는다.
                change += 1
                stk.append('{')
        else : 
            stk.append('{') # 여는 괄호는 스택에 넣는다.     
    
    res.append(len(stk)//2 + change) # 스택에 남아있는 여는 괄호 중 절반을 닫는 괄호로 변경 + 닫는 괄호를 여는 괄호로 변경한 횟수 

for i in range(len(res)) :
    print("{}. {}".format(i+1, res[i]))
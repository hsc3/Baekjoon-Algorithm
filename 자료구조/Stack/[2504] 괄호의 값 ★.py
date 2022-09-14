# [2504] 괄호의 값 | Silver 1 | 자료구조(Stack)
'''
4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.
ㆍ 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
ㆍ 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
ㆍ X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.

우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.
ㆍ ‘()’ 인 괄호열의 값은 2이다.
ㆍ ‘[]’ 인 괄호열의 값은 3이다.
ㆍ ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
ㆍ ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
ㆍ 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.

여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.
첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.
'''
import sys
input = sys.stdin.readline
data = input().rstrip()

stk = []
answer = 0
num = 1
for i in range(len(data)):
    # 여는 괄호 -> 스택에 삽입
    if data[i] == '(':
        stk.append(data[i])
        num *= 2
    elif data[i] == '[':
        stk.append(data[i])
        num *= 3
    # 닫는 괄호 -> 스택의 맨 뒤 괄호와 비교
    elif data[i] == ')':
        if not stk or stk[-1] == '[': # 잘못된 문자열의 케이스
            answer = 0
            break
        elif data[i-1] == '(': # 괄호의 쌍 완성 -> answer에 num 누적
            answer += num
        stk.pop()
        num //= 2
    else:
        if not stk or stk[-1] == '(':
            answer = 0
            break
        elif data[i-1] == '[':
            answer += num
        stk.pop()
        num //= 3

print(answer if not stk else 0)
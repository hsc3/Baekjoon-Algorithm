'''
[12904] A와 B / Gold 5 / 문자열, 그리디
A와 B로만 이루어진 영어 단어가 존재한다. 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임을 진행한다. 
문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.
- 문자열의 뒤에 A를 추가한다.
- 문자열을 뒤집고 뒤에 B를 추가한다.
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 
'''
# T -> S ; 역으로 접근하기

import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while len(S) != len(T) :
    if T[-1] == 'A' :
        T.pop() # 문자열의 뒤 A를 제거
    else :
        T.pop() # 문자열의 뒤 B를 제거한 후, 뒤집는다.
        T.reverse()
        
print(1) if S == T else print(0)


# 시간초과 난 케이스.
'''
import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while len(S) != len(T) :
    if T[-1] == 'A' :
        T = T[:-1]
    else :
        T = T[1::-1]

print(1) if S == T else print(0)
'''
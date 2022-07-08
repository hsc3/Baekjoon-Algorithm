'''
[3613] Java vs C++ / Silver 3 / 문자열, 파싱, 구현
Java에서는 변수의 이름이 여러 단어로 이루어져있을 때, 다음과 같은 방법으로 변수명을 짓는다.
첫 단어는 소문자로 쓰고, 다음 단어부터는 첫 문자만 대문자로 쓴다. 또, 모든 단어는 붙여쓴다.
따라서 Java의 변수명은 javaIdentifier, longAndMnemonicIdentifier, name, bAEKJOON과 같은 형태이다.

반면에 C++에서는 변수명에 소문자만 사용한다. 단어와 단어를 구분하기 위해서 밑줄('_')을 이용한다.
C++ 변수명은 c_identifier, long_and_mnemonic_identifier, name, b_a_e_k_j_o_o_n과 같은 형태이다.

프로그램은 가장 먼저 변수명을 입력으로 받은 뒤, 이 변수명이 어떤 언어 형식인지를 알아내야 한다.
그 다음, C++형식이라면 Java형식으로, Java형식이라면 C++형식으로 바꾸면 된다. 만약 C++형식과 Java형식 둘 다 아니라면, 에러를 발생시킨다.
'''
def Error() :
    print("Error!")
    exit(0)

def JavaToCpp(variable) :
    parsed = list(variable.rstrip())
    for i in range(len(parsed)):
        if parsed[i].isupper(): # 대문자 알파벳을 "_ + 소문자 알파벳"으로 변경
            parsed[i] = '_' + parsed[i].lower()

    return ''.join(parsed)

def CppToJava(variable) :
    parsed = list(variable.split('_'))
    for i in range(len(parsed)):
        if len(parsed[i]) == 0: # _가 연속으로 사용된 경우 혹은 마지막에 _가 있는 경우
            Error()
        for word in parsed[i]:
            if word.isupper() :
                Error()
        if i != 0: # 파싱된 문자열의 첫번째를 제외하고 "_ + 소문자 알파벳" 형태를 대문자 알파벳으로 변경
            parsed[i] = parsed[i][0].upper() + parsed[i][1:]

    return ''.join(parsed)

import sys
input = sys.stdin.readline
variable = input().rstrip()
if variable[0] == '_' or variable[0].isupper() :
    Error()
print(CppToJava(variable) if '_' in variable else JavaToCpp(variable))
'''
[2789] 유학 금지 / Bronze 2 / 문자열
이메일의 각 단어 중에서 CAMBRIDGE에 포함된 알파벳은 모두 지우기로 했다.
어떤 단어가 주어졌을 때, 검열을 거친 후에는 어떤 단어가 되는지 구하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

ban = "CAMBRIDGE"
string = input().rstrip()

res = ""
for s in string :
    if s in ban :
        continue
    else :
        res += s

print(res)

'''
string = input()

for s in 'CAMBRIDGE':
    string = string.replace(s, '')

print(string)
'''

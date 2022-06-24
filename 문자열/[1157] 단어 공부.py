'''
[1157] 단어 공부 / Bronze 1 / 문자열
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
'''

import sys
input = sys.stdin.readline

alphabet = [[0, i] for i in range(26)] 

string = input().rstrip() 

for char in string:
    if char.isupper(): # 대문자: 65 - 90
        alphabet[ord(char)-65][0] += 1
    else: # 소문자: 97 - 122
        alphabet[ord(char)-97][0] += 1

alphabet.sort(reverse = True)
print("?" if alphabet[0][0] == alphabet[1][0] else chr(alphabet[0][1]+65))
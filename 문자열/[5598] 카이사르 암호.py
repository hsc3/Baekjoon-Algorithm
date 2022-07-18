'''
[5598] 카이사르 암호 / Bronze 2 / 문자열 
가이우스 율리우스 카이사르(Gaius Julius Caesar)는 고대 로마 군인이자 정치가였다.
카이사르는 비밀스럽게 편지를 쓸 때, 'A'를 'D로', 'B'를 'E'로, 'C'를 'F'로... 이런 식으로 알파벳 문자를 3개씩 건너뛰어 적었다고 한다.
26개의 대문자 알파벳으로 이루어진 단어를 카이사르 암호 형식으로 3문자를 옮겨 겹치지 않게 나열하여 얻은 카이사르 단어가 있다.
이 카이사르 단어를 원래 단어로 돌려놓는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

caesarLetters = input().rstrip()

answer = ''
for letter in caesarLetters:
    asciiNum = ord(letter) - 3
    if asciiNum < 65: # A (65) ~ Z (90)
        asciiNum += 26
    answer += chr(asciiNum)

print(answer)


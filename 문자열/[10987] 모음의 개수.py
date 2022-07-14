'''
[10987] 모음의 개수 / Bronze 2 / 문자열
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 모음(a, e, i, o, u)의 개수를 출력하는 프로그램을 작성하시오.
'''
import sys
from collections import Counter

input = sys.stdin.readline

string = input().rstrip()
vowel = ['a', 'e', 'i', 'o', 'u']


counterString = Counter(string)
answer = 0
for key, value in counterString.items():
    if key in vowel: # key가 모음일 경우, 갯수(value)를 합산합니다.
        answer += value

print(answer)
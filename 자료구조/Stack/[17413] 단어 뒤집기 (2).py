# [17413] 단어 뒤집기 (2) | Silver 3 | 자료구조(stack)
'''
문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다. 먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.
- 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
- 문자열의 시작과 끝은 공백이 아니다.
- '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다.
단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.
'''
import sys
input = sys.stdin.readline
from collections import deque

str = input().rstrip()
q = deque()

res = ''
tag = False
for chr in str:
    if tag: # tag 입력 상태인 경우
        res += chr
        if chr == '>':
            tag = False # tag 입력 종료

    else: # tag 입력 상태가 아닌 경우
        if chr == ' ':
            while q:
                res += q.pop() # 스택에 저장된 이전 문자열을 뒤집어서 저장한다.
            res += chr
        elif chr == '<': # tag 입력 상태가 시작되는 경우
            while q:
                res += q.pop()
            tag = True
            res += chr
        else: # 문자열을 입력받는 경우, 스택에 저장한다.
            q.append(chr)

while q:
    res += q.pop()
print(res)

# import sys
# word = list(sys.stdin.readline().rstrip())
# i = 0
# start = 0
#
# while i < len(word):
#     if word[i] == "<": # tag는 뒤집지 않고 그대로 유지
#         i += 1
#         while word[i] != ">": i += 1
#         i += 1
#     elif word[i].isalnum(): # 문자열의 시작점
#         start = i
#         while i < len(word) and word[i].isalnum(): i += 1
#         rev = word[start:i]
#         rev.reverse()
#         word[start:i] = rev
#     else: i += 1 # 공백인 경우
#
# print("".join(word))

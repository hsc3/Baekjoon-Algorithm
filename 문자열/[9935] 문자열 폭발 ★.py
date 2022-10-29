# [9935] 문자열 폭발 | Gold 4 | https://www.acmicpc.net/problem/9935
# 스택에 문자를 하나씩 넣다가 ""폭발 문자열의 가장 뒤 문자와 일치하는 경우""에만, 스택에 담긴 문자열과 폭발 문자열을 비교
import sys
input = sys.stdin.readline

myStr = list(input().rstrip())
bomb = list(input().rstrip())
L = len(bomb)
stk = []
for chr in myStr:
    stk.append(chr)
    if chr == bomb[-1]: # 폭발 문자열의 마지막 문자와 일치하는 경우
        if stk[-L:] == bomb: # 스택의 뒤에서부터 폭발 문자열의 길이만큼을 비교
            del stk[-L:] # 같으면 제거

print(''.join(stk) if stk else 'FRULA')
# [1254] 팰린드롬 만들기 | Silver 2 | 문자열
'''
규완이는 팰린드롬을 엄청나게 좋아한다. 팰린드롬이란 앞에서부터 읽으나 뒤에서부터 읽으나 같게 읽히는 문자열을 말한다.
동호는 규완이를 위한 깜짝 선물을 준비했다. 동호는 규완이가 적어놓고 간 문자열 S에 0개 이상의 문자를 문자열 뒤에 추가해서 팰린드롬을 만들려고 한다.
동호는 가능하면 가장 짧은 문자열을 만들려고 한다. 동호가 만들 수 있는 가장 짧은 팰린드롬의 길이를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

S = list(input().rstrip()) # abab
revS = S[::-1] # baba

answer = 0
for i in range(len(S)):
    if S[i:] == revS[:len(S)-i]: # S와 revS의 부분 문자열이 겹치는 경우 (S와 revS의 겹치는 최장 부분 문자열을 구해야 한다.)
        answer = i + len(S)
        break

print(answer)
# abab
#  baba
# ------
# ababa

# qwerty
#      ytrewq
# ------------
# qwertytrewq
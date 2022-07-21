'''
[1543] 문서 검색 / Silver 4 / 문자열, 그리디, 브루트포스
세준이는 영어로만 이루어진 어떤 문서를 검색하는 함수를 만들려고 한다.
이 함수는 어떤 단어가 총 몇 번 등장하는지 세려고 한다.
문서와 검색하려는 단어가 주어졌을 때, 그 단어가 최대 몇 번 중복되지 않게 등장하는지 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

a = input().rstrip() # ababababa
b = input().rstrip() # aba

answer = 0
idx = 0 # 문자열 a에서 검색하고 있는 현 인덱스
while idx <= len(a) - len(b) + 1 :
    if a[idx:idx+len(b)] == b :
        answer += 1
        idx += len(b)
    else :
        idx += 1

print(answer)
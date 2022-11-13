# [2671] 잠수함식별 | Gold 5 | https://www.acmicpc.net/problem/2671
import sys
input = sys.stdin.readline
import re # 정규표현식 지원

''' 정규표현식
- import re
- pattern = re.compile(정규표현식)
- pattern.fullmatch()

정규표현식 : (100~1~|01)~ -> (100+1+|01)+
'''

data = str(input().rstrip())
pattern = re.compile('(100+1+|01)+') # 정규표현식에 해당하는 패턴 컴파일
answer = pattern.fullmatch(data) # 패턴에 일치하는지 여부

print("SUBMARINE" if answer else "NOISE")
'''
[5988] 홀수일까 짝수일까 / Bronze 3 / 문자열
짝이 없는 경재는 매일 홀로 있다보니 홀수를 판별할 수 있는 능력이 생겼다.
창식이는 경재의 말이 사실인지 그 능력을 시험해보려 한다. 창식이의 의심이 끝이 없을 것 같아 N개만 확인하기로 정했다.
N개의 정수가 주어지면 홀수인지 짝수인지를 출력하는 프로그램을 만들어 경재의 능력을 검증할 수 있게 도와주자.
'''

import sys
input = sys.stdin.readline

res = []
for _ in range(int(input())) :
    res.append("even") if int(input()) % 2 == 0 else res.append("odd")

print(*res, sep='\n') 

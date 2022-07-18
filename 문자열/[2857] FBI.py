'''
[2857] FBI / Bronze 3 / 문자열
5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.
FBI요원은 요원의 첩보원명에 FBI가 들어있다.
'''
import sys
input = sys.stdin.readline

answer = []
for i in range(1, 6):
    codeName = input().rstrip()
    if 'FBI' in codeName:
        answer.append(i)

if len(answer) == 0:
    print("HE GOT AWAY!")
else:
    print(*answer)
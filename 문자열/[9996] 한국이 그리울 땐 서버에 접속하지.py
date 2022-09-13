# [9996] 한국이 그리울 땐 서버에 접속하지 | Silver 3 | 문자열
'''
패턴은 알파벳 소문자 여러 개와 별표(*) 하나로 이루어진 문자열이다.
파일 이름이 패턴에 일치하려면, 패턴에 있는 별표를 알파벳 소문자로 이루어진 임의의 문자열로 변환해 파일 이름과 같게 만들 수 있어야 한다.
별표는 빈 문자열로 바꿀 수도 있다. 예를 들어, "abcd", "ad", "anestonestod"는 모두 패턴 "a*d"와 일치한다. 하지만, "bcd"는 일치하지 않는다.
패턴과 파일 이름이 모두 주어졌을 때, 각각의 파일 이름이 패턴과 일치하는지 아닌지를 구하는 프로그램을 작성하시오.
총 N개의 줄에 걸쳐서, 입력으로 주어진 i번째 파일 이름이 패턴과 일치하면 "DA", 일치하지 않으면 "NE"를 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
pattern = list(map(str, input().rstrip()))

# 1. '*' 기준 왼쪽과 오른쪽 패턴을 구한다.
leftPattern, rightPattern = '', ''
index = pattern.index('*')
leftPattern = ''.join(pattern[:index])
rightPattern = ''.join(pattern[index+1:])
ll = len(leftPattern)
rl = len(rightPattern)

answer = []
for _ in range(N):
    fileName = input().rstrip() # 문자열 입력
    # 2. 입력받은 문자열에서 패턴을 비교한다.
    if len(fileName) >= ll + rl and leftPattern == fileName[:ll] and rightPattern == fileName[::-1][:rl][::-1]:
        answer.append("DA")
    else:
        answer.append("NE")

print(*answer, sep='\n')



'''
[2331] 반복 수열 / Silver 4 / 구현
다음과 같이 정의된 수열이 있다.
D[1] = A
D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합
예를 들어 A=57, P=2일 때, 수열 D는 [57, 74(=5^2+7^2=25+49), 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, …]이 된다.
그 뒤에는 앞서 나온 수들(57부터가 아니라 58부터)이 반복된다.

이와 같은 수열을 계속 구하다 보면 언젠가 이와 같은 반복수열이 된다. 이때, 반복되는 부분을 제외했을 때, 수열에 남게 되는 수들의 개수를 구하는 프로그램을 작성하시오.
위의 예에서는 [57, 74, 65, 61]의 네 개의 수가 남게 된다.
'''
import sys
input = sys.stdin.readline

A, P = map(int, input().split())
D = [A]
# 수열에 저장된 이전 숫자들과 같은 숫자가 만들어지면 반복 수열이 시작되는 부분에 해당한다.
while True:
    prevNum = D[-1] # 이전 숫자, int 형
    currNum = 0 # 현재 (만들어지는) 숫자, int 형
    for n in str(prevNum):
        currNum += int(n) ** P
    if currNum in D: # 수열에 저장된 이전 숫자들과 같은 숫자인 경우
        repeatStartIdx = D.index(currNum) # 반복 수열이 시작되는 인덱스를 탐색
        D = D[:repeatStartIdx]
        break
    else:
        D.append(currNum)

print(len(D))
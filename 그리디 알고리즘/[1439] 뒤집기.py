# [1439] 뒤집기 / Silver 5 / 그리디 알고리즘
'''
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다.
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

예를 들어 S=0001100 일 때,
전체를 뒤집으면 1110011이 된다.
4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.
'''
import sys
input = sys.stdin.readline

string = list(input().rstrip())
answer = 0 # 뒤집는 횟수

prevNum = string[0] # 이전 문자
for i in range(1, len(string)):
    if prevNum != string[i]: # 이전 문자와 다음 문자가 다른 경우
        for j in range(i+1, len(string)):  # 이전 문자와 같은 문자가 나올때까지 탐색
            if prevNum == string[j]:
                string[i:j+1] = prevNum * (j-i+1) # 문자열을 뒤집는다.
                break
        prevNum = string[i] # 이전 문자 업데이트
        answer += 1

print(answer)


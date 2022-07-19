'''
[5525] IOIOI / Silver 1 / 문자열
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = str(input().rstrip())
# 1. PN을 만든다.
PN = 'IO' * N + 'I'

answer = 0
# 2. S에 포함되어 있는 PN의 개수를 센다.
startIdx = 0
cnt = 0
while startIdx < M - 1:
    if S[startIdx:startIdx+3] == "IOI": # IOI의 연속되는 횟수를 계산한다.
        cnt += 1
        startIdx += 2
        if cnt == N:
            answer += 1
            cnt -= 1

    else:
        startIdx += 1
        cnt = 0

print(answer)

'''
OOIOIOIOIIOII
OO/I/O/I/O/I/O/II/O/II
  IOI
    IOI
      IOI
         IOI
'''
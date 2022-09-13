# [15353] 큰 수 A+B (2) | Silver 4 | 문자열
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

A, B = input().split()
# 1. 두 숫자의 길이를 동일하게 만든다.
while len(A) != len(B):
    if len(A) < len(B):
        A = '0' + A
    else:
        B = '0' + B

# 2. 두 숫자의 각 자리수별로 덧셈을 수행한다.
remain = 0 # 두 숫자의 이전 자리수 덧셈에서 넘어오는 값
answer = '' 
while A and B:
    result = str(int(A[-1]) + int(B[-1]) + remain) # 덧셈 수행
    A = A[:len(A)-1] # 덧셈을 수행한 A의 숫자 제거
    B = B[:len(B)-1] # 덧셈을 수행한 B의 숫자 제거
    if len(result) == 2: # 덧셈 수행 결과, 넘어가는 숫자가 발생하는 경우
        answer += result[1]
        remain = int(result[0])
    else: # 덧셈 수행 결과, 넘어가는 숫자가 발생하지 않는 경우
        answer += result[0]
        remain = 0

if remain:
    answer += str(remain)

print(answer[::-1])



'''
[5430] AC / Gold 5 / 구현, 자료 구조(Deque), 문자열, 파싱
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.
배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.
'''

import sys ; 
input = sys.stdin.readline
from collections import deque
# ===========================================
def Operator(operation, l) :
    rev = 0 # count for doing reverse 
     
    for o in operation :
        if o == "R" :
            rev += 1

        elif o == "D" :
            if rev % 2 == 0 :
                l.popleft()  
            else :
                l.pop()

    if rev % 2 == 1 :
        l.reverse()    
    
    return "[" + ",".join(l) + "]"

# ===========================================
answer = []

for i in range(int(input())) :
    operation = input()   # RDD
    n = int(input())      # 4
    l = deque(list(input().rstrip()[1:-1].split(',')))  # [1,2,3,4]

    if n < operation.count('D') : 
        answer.append("error")
        continue
    
    answer.append(Operator(operation, l))

print(*answer, sep = '\n')
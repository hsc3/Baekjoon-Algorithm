# 문자열, 큐 [5430] AC | https://www.acmicpc.net/problem/5430

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
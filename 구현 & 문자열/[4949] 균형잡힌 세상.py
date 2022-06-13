# 문자열 [4949] 균형잡힌 세상 | https://www.acmicpc.net/problem/4949
from collections import deque
'''
answer = []
while True :
    string = input()
    if string == '.' : break
    else :
        queue = []
        error = False
        for s in string :
            if s == '[' or s == '(' :
                queue.append(s)
            elif s == ']' or s == ')' :
                if not queue :
                    answer.append("no")
                    error = True
                    break 
                else :
                    prev = queue.pop()
                    if s == ']' and prev == '(' :
                        answer.append("no")
                        error = True
                        break
                    elif s == ')' and prev == '[' :
                        answer.append("no")
                        error = True
                        break
        if not error :
            if queue : answer.append("no")
            else :     answer.append("yes")

print(*answer, sep = '\n')

'''
import sys
input = sys.stdin.readline
result = []
while True:
    x = input().rstrip()
    assert(x[-1]=='.') # 해당 조건을 보장
    if x == ".": # while문의 종료 조건
        break

    stk = []
    open = {"(":")", "[":"]"}
    close = {")", "]"}
    flag = True
    for i in x:
        if i in open: # ( 또는 [ 문자인 경우
            stk.append(i)
        elif i in close: # ) 또는 ] 문자인 경우
            if stk and i == open[stk.pop()]:
                continue
            else:
                flag = False
                break
    if stk:
        flag = False
    result.append("yes") if flag else result.append("no")

print(*result, sep = '\n')
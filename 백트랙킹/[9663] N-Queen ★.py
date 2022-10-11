# [9663] N-Queen | Gold 4 | https://www.acmicpc.net/problem/9663

def check(queens, x, y):
    for queen in queens:
        if abs(queen[0] - x) == abs(queen[1] - y):
            return False
    return True

def makeQueen(queens, prev_y, x):
    global answer
    if x == N:
        answer += 1
        return

    for y in range(N): # 각 행(x)마다 하나의 퀸을 놓을 수 있다.
        if x == 0:
            makeQueen(queens + [[x, y]], prev_y + [y], x+1)
        # 이전의 퀸이 놓인 열(prev_y)에는 놓을 수 없다.
        # 이전의 퀸과 대각선에 놓이는지 체크
        elif y not in prev_y and check(queens, x, y):
            makeQueen(queens + [[x, y]], prev_y + [y], x+1)

answer = 0
N = int(input())
makeQueen([], [], 0)
print(answer)
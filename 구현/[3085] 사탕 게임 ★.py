# [3085] 사탕 게임 | Silver 3 | 구현
'''
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
가장 처음에 N×N 크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다.
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P,
'''
import sys
input = sys.stdin.readline

def CheckBoard(board): # 보드의 사탕 색깔을 바꿔서 검사하는 함수 (바꾸지 않는 경우 포함)
    global answer
    # [1] 사탕 색상을 바꾸지 않고 검사
    answer = max(answer, CountSameColor([*board]))

    # [2] 사탕 색상을 바꾸면서 검사
    for i in range(N):
        for j in range(N-1):
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 색상 변경

            # 색상이 바뀐 사탕이 포함된 row 1줄과 column 2줄을 검사해야 한다.
            lines = []
            lines.append(board[i])
            lines.append([board[k][j] for k in range(N)])
            lines.append([board[k][j+1] for k in range(N)])

            answer = max(answer, CountSameColor(lines)) # 먹을 수 있는 사탕의 최대 개수 저장
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 바꾼 색상 초기화

def CountSameColor(line): # 한 줄의 row 혹은 column 내에서 연속된 같은 색상의 사탕 수를 찾는다.
    maxColor = 1

    for l in line:
        cnt = 1
        for i in range(N-1):
            if l[i] == l[i+1]: # 인접한 두 사탕의 색상이 같은 경우
                cnt += 1
            else: # 인접한 두 사탕의 색상이 다른 경우
                maxColor = max(maxColor, cnt)
                cnt = 1
        maxColor = max(maxColor, cnt)

    return maxColor

def ChangeBoard(board): # 보드의 행과 열을 변환해주는 함수
    changedBoard = []
    for tuple in zip(*board):
        changedBoard.append(list(tuple))
    return changedBoard

if __name__ == "__main__":
    N = int(input())
    board = [list(input().rstrip()) for _ in range(N)]

    answer = 0
    CheckBoard(board) # 보드 그대로 검사
    CheckBoard(ChangeBoard(board)) # 보드의 행과 열을 변환한 후 검사
    print(answer)


'''
import sys
import copy
input = sys.stdin.readline
def CheckBoard(board): # 보드의 row와 column을 모두 검사한다.
    global answer

    for i in range(N): # 행 기준
        for j in range(N-1):
            copiedBoard = copy.deepcopy(board)
            # 사탕 색상 변경
            colorA = copiedBoard[i][j]
            copiedBoard[i][j] = copiedBoard[i][j+1]
            copiedBoard[i][j+1] = colorA

            # 색상을 바꾼 row, column의 사탕 색상 검사
            line1 = copiedBoard[i]
            line2 = [copiedBoard[k][j] for k in range(N)]
            line3 = [copiedBoard[k][j+1] for k in range(N)]

            maximumColorCnt = CountSameColor(line1, line2, line3)
            answer = max(answer, maximumColorCnt)

def CountSameColor(l1, l2, l3): # 한 줄의 row 혹은 column 내에서 같은 색상의 사탕 수를 찾는다.
    maximum = 1

    for l in l1, l2, l3:
        color = l[0] # 맨 앞 사탕의 색상
        cnt = 1
        for i in range(1, N): # 이후 사탕들을 탐색
            if l[i] == color: # 인접한 두 사탕의 색상이 같은 경우
                cnt += 1
                maximum = max(maximum, cnt)
            else: # 인접한 두 사탕의 색상이 다른 경우
                cnt = 1
                color = l[i]

    return maximum

def ChangeBoard(board):
    changedBoard = []
    for tuple in zip(*board):
        changedBoard.append(list(tuple))
    return changedBoard

if __name__ == "__main__":
    N = int(input())
    board = [list(input().rstrip()) for _ in range(N)]

    answer = 0
    CheckBoard(board) # row 검사
    CheckBoard(ChangeBoard(board)) # column 검사
    print(answer)
'''
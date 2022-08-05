# [2578] 소수 | Silver 4 | 구현
'''
빙고 게임은 다음과 같은 방식으로 이루어진다.
1. 먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다.
2. 다음은 사회자가 부르는 수를 차례로 지워나간다.
3. 차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.
4. 이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.

철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

# 빙고판에서 사회자가 부른 숫자 제거
def eraseNumber(number): 
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = 0
                return i, j # 숫자의 인덱스

# 빙고판에서 체크한 줄의 수 체크
def bingo(i, j):
    global chk

    if i == j and [board[k][k] for k in range(0, 5)].count(0) == 5: # ↘ 체크
        chk += 1
    if i + j == 4 and [board[k][4-k] for k in range(0, 5)].count(0) == 5: # ↗ 체크
        chk += 1
    if [board[i][k] for k in range(0, 5)].count(0) == 5: # → 체크
        chk += 1
    if [board[k][j] for k in range(0, 5)].count(0) == 5: # ↓ 체크
        chk += 1

    return True if chk >= 3 else False


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(5)] # 철수의 빙고판
    numbers = [] # 부르는 수의 순서
    for _ in range(5):
        numbers += list(map(int, input().split()))

    chk = 0 # 모두 체크된 줄의 수
    answer = 0
    for number in numbers:
        i, j = eraseNumber(number)
        answer += 1
        if bingo(i, j):
            break

    print(answer)



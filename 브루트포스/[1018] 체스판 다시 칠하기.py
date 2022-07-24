# [1018] 체스판 다시 칠하기 / Silver 4 / 브루트포스 알고리즘
'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''
# MxN 크기의 보드에서 어떠한 부분이든지 8x8 크기의 하나의 체스판을 만드는 문제이다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = [list(input().rstrip()) for _ in range(N)]
color = ['B', 'W'] # 체스 말의 색깔

answer = 64 # 8x8 체스 판에서 다시 칠해야 하는 칸의 수

for i in range(N-7):
    for j in range(M-7):
        recolorB, recolorW = 0, 0 # 첫번째 칸의 색깔을 기준(B or W)으로 다시 칠해야 하는 횟수
        for row in range(8):
            for col in range(8):
                if chess[i+row][j+col] != color[(row+col)%2]: # 체스 말의 좌표의 합이 짝수 or 홀수인 것끼리 색깔이 같아야 한다.
                    recolorB += 1
                else:
                    recolorW += 1

        answer = min(recolorB, recolorW, answer)
            
print(answer)
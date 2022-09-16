# [2630] 색종이 만들기 | Silver 2 | 분할정복
'''
여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다.
전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다.
이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.
하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어진다.
입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def conquer(size, x, y):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != color:
                return False
    if color == 0:
        white += 1
    else:
        blue += 1
    return True


def divide(size, x, y):
    if conquer(size, x, y):
        return

    divide(size//2, x, y)
    divide(size//2, x, y+size//2)
    divide(size//2, x+size//2, y)
    divide(size//2, x+size//2, y+size//2)

if __name__ == "__main__":
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    white, blue = 0, 0
    divide(N, 0, 0)
    print(white)
    print(blue)
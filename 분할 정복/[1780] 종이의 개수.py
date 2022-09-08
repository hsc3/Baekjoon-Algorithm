# [1780] 종이의 개수 | Silver 2 | 분할 정복, 재귀
'''
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.
(1) 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
(2) (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline 

# Conquer : 잘린 종이의 숫자 확인
def Conquer(x, y, size):

    global answer
    num = paper[x][y]
    
    # 종이의 각 칸의 숫자 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != num:
                return False # 더 작은 문제로 분할해야 한다.

    # 부분 문제의 정답 도출 
    if num == -1:
        answer[0] += 1
    elif num == 0:
        answer[1] += 1
    else:
        answer[2] += 1

    return True

# Divide : 종이가 같은 숫자로 채워지지 않은 경우, 더 작은 종이로 분할
def Divide(x, y, size):

    if Conquer(x, y, size): # 종이의 모든 칸이 같은 숫자인 경우 -> 분할X
        return

    # 종이의 모든 칸이 같은 숫자가 아닌 경우 -> 더 작은 문제로 분할
    for xx in range(x, x + size, size // 3):
        for yy in range(y, y + size, size // 3):
            Divide(xx, yy, size // 3)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]
Divide(0, 0, N)
print(*answer, sep='\n')
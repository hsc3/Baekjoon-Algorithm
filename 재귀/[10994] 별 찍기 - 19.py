# [10994] 별 찍기 - 19 | Silver 4 | https://www.acmicpc.net/problem/10994

def recur(size, point): # size: 사각형 변의 길이, point: 사각형 왼쪽 위의 꼭지점
    if size < 1:
        return

    for i in range(size):
        arr[point+i][point] = '*' # 왼쪽 면
        arr[point+i][point+size-1] = '*'# 오른쪽 면
        arr[point][point+i] = '*' # 윗쪽 면
        arr[point+size-1][point+i] = '*' # 아래쪽 면

    return recur(size-4, point+2)

N = int(input())
arr = [[' ' for _ in range(4*N-3)] for _ in range(4*N-3)]
recur(4*N-3, 0)

for row in arr:
    print(''.join(row))
'''
[1932] 정수 삼각형 / Silver 1 / 다이나믹 프로그래밍
맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
'''
import sys
input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N) :
    for j in range(i+1) :
        # 정수 삼각형의 각 층에서 가장 왼쪽과 가장 오른쪽의 숫자, 그리고 가운데의 숫자로 경우의 수를 나누어 규칙을 생성
        if j == 0 :
            triangle[i][j] += triangle[i-1][j]
        elif i == j :
            triangle[i][j] += triangle[i-1][j-1]
        else :
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[N-1]))
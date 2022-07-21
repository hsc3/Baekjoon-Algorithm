# [2563] 색종이 / Bronze 1 / 구현
# 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
import sys; input = sys.stdin.readline

res = 0
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(int(input())) :
    y, x = map(int, input().split())
    for i in range(x, x+10) :
        for j in range(y, y+10) :
            if paper[i][j] == 0 :
                res += 1
                paper[i][j] = 1

print(res)
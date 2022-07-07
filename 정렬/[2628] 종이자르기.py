'''
[2628] 종이자르기 / Silver 5 / 정렬
입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

width, height = map(int, input().split())
x, y = [width, 0], [height, 0] # 가로, 세로

for _ in range(int(input())) :
    direction, cutPoint = map(int, input().split())
    # 종이를 자르는 점선의 지점을 저장한다.
    if direction == 0 : # 가로로 자르는 점선
        y.append(cutPoint)
    elif direction == 1 : # 세로로 자르는 점선
        x.append(cutPoint)

x.sort(reverse = True);
y.sort(reverse = True);
# 종이를 잘랐을 때, 가장 큰 종이 조각의 가로와 세로의 길이를 구한다.
maxX = max([x[i]-x[i+1] for i in range(len(x)-1)])
maxY = max([y[i]-y[i+1] for i in range(len(y)-1)])

print(maxX*maxY)
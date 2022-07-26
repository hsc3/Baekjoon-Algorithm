# [2304] 창고 다각형 | Silver 2 | 브루트포스, 자료구조(stack)
'''
개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1 m이며 높이는 다를 수 있다. 이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다.
창고에는 모든 기둥이 들어간다. 이 창고의 지붕을 다음과 같이 만든다.
1. 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
4. 지붕의 가장자리는 땅에 닿아야 한다.
5. 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
width = 0
max_height = 0
max_column_idx = 0
data = []

for _ in range(N) :
    idx, height = map(int, input().split())
    data.append([idx, height])
    if idx > width :
        width = idx
    if height > max_height :
        max_height = height
        max_column_idx = idx
# data = [[2,4] , [4,6] , [5,3] , [8,10] , [11,4] , [13,6] , [15,8]]
# --------------------------------------------------------------
columns = [0] * (width+1)
for i in range(len(data)) :
    columns[data[i][0]] = data[i][1]

# columns = [0, 0, 4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8]
#      ---> [0 ,0, 4, 4, 6, 6, 6, 6, 10, 8, 8, 8, 8, 8, 8, 8]

tmp = 0
for i in range(max_column_idx) :
    if columns[i] > tmp :
        tmp = columns[i]
    else :
        columns[i] = tmp
tmp = 0
for i in range(width, max_column_idx-1, -1) :
    if columns[i] > tmp :
        tmp = columns[i] 
    else :
        columns[i] = tmp

print(sum(columns))
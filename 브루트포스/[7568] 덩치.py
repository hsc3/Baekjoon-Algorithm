# [7568] 덩치 / Silver 5 / 브루트포스

import sys
input = sys.stdin.readline

N = int(input())
data = []
res = [0] * N

for i in range(N) :
    weight, height = map(int, input().split())
    data.append([weight, height])

for i in range(N) :
    bigPeople = 0 # 자신보다 덩치가 큰 사람의 수
    for j in range(N) :
        if data[i][0] < data[j][0] and data[i][1] < data[j][1] :
            bigPeople += 1
    print(bigPeople+1, end = ' ')
        
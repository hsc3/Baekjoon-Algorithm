'''
[11650] 좌표 정렬하기 / Silver 5 / 정렬
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

axis = []
for _ in range(int(input())) :
    axis.append(list(map(int, input().split())))

axis.sort(key = lambda x : (x[0], x[1]))

for a in axis : 
    print(*a)
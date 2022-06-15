'''
[11651] 좌표 정렬하기 (2) / Silver 5 / 정렬
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, 
y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

axisList = []
for _ in range(int(input())) :
    axisList.append(list(map(int, input().split())))

axisList.sort(key = lambda x : (x[1], x[0])) # y좌표가 증가하고, 같을 경우 x좌표가 증가하는 순으로 정렬

for axis in axisList :
    print(*axis)
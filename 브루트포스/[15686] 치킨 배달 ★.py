'''
[15686] 치킨 배달 / Gold 5 / 브루트포스
크기가 N×N인 도시가 있다. 0은 빈 칸, 1은 집, 2는 치킨집이다. 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다. 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.
'''
import sys, itertools
input = sys.stdin.readline
N, M = map(int, input().split()) # 도시의 크기, 폐업하지 않을 치킨집의 수 
city, chicken, home = [], [], []
# 치킨집과 가정집의 좌표 저장
for i in range(N) :
    city = list(map(int, input().split()))
    for j in range(N) :
        if city[j] == 1 :
            home.append([i,j])
        elif city[j] == 2 :
            chicken.append([i,j])
# M개의 치킨집 조합 생성
shortest_distance = float("inf")
for safeChicken in itertools.combinations(chicken, M) :
    distance = 0
    for i in range(len(home)) :
        d = float("inf")
        for j in range(len(safeChicken)) :
            d = min(d, abs(home[i][0]-safeChicken[j][0])+abs(home[i][1]-safeChicken[j][1]))
        distance += d
    shortest_distance = min(shortest_distance, distance)
print(shortest_distance)

'''
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = []
home = []
chicken = []

for i in range(N):
  city.append(list(map(int, input().split())))
  for j in range(N):
    if city[i][j] == 1:
      home.append((i, j))
    elif city[i][j] == 2:
      chicken.append((i, j))

dist = [[] for _ in range(len(home))]

for i, (hx, hy) in enumerate(home):
  for cx, cy in chicken:
    dist[i].append(abs(hx-cx) + abs(hy-cy))

answer = []
for picks in list(combinations(range(len(chicken)), M)):
  test = 0
  for d in dist:
    t = []
    for p in picks:
      t.append(d[p])
    test += min(t)
  answer.append(test)

print(min(answer))
'''
# [1004] 어린 왕자 | Silver 3 | https://www.acmicpc.net/problem/1004
import sys
input = sys.stdin.readline

def atPlanet(px, py, r, x, y): # (x, y)가 행성의 경계 내에 포함되는지 판별
    distance = (px - x) ** 2 + (py - y) ** 2 
    if distance <= r ** 2:
        return True
    return False

answer = []
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    planets = [list(map(int, input().split())) for _ in range(int(input()))]
    cnt = 0
    for px, py, r in planets:
        cnt += abs(atPlanet(px, py, r, x1, y1)- atPlanet(px, py, r, x2, y2))
    answer.append(cnt)

print(*answer, sep='\n')


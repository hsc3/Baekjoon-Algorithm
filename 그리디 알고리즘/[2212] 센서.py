# [2212] 센서 | Gold 5 | https://www.acmicpc.net/problem/2212

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))
distance = sorted([sensor[i] - sensor[i-1] for i in range(1, N)], reverse=True) # 센서 거리를 내림차순으로 정렬

print(sum(distance[K-1:]))

'''
sensor = [1, 3, 6, 6, 7, 9]
distance = [2, 3, 0, 1, 2] -> [3, 2, 2, 1, 0] 
집중국의 개수가 2개이면, 센서 사이의 거리 1개를 포함하지 않을 수 있다. 가장 거리가 먼 센서 사이의 거리를 포함하지 않는다.
'''
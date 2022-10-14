# [13164] 행복 유치원 | Gold 5 | https://www.acmicpc.net/problem/13164

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
students = sorted(list(map(int, input().split())))

# 아이들의 키 차이를 저장한다. (내림차순)
data = sorted([students[i] - students[i-1] for i in range(1, N)], reverse=True)
print(sum(data[K-1:])) # 키 차이가 많이 나는 인접한 아이들은 같은 팀으로 배정 -> data에서 가장 큰 값 K-1개를 제외할 수 있다.
# [19941] 햄버거 분배 | Silver 3 | 그리디 알고리즘
'''
기다란 벤치 모양의 식탁에 사람들과 햄버거가 아래와 같이 단위 간격으로 놓여 있다. 사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있다.
식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K, 사람과 햄버거의 위치가 주어졌을 때, 햄버거를 먹을 수 있는 사람의 최대 수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = list(input().rstrip())
eat = [False for _ in range(N)]

answer = 0
for i in range(len(table)):
    if table[i] == 'P': # 사람 -> K 범위 내 테이블 왼쪽에서부터 아직 먹지 않은 첫 번째 햄버거를 먹는다.
        for j in range(i-K, i+K+1):
            if 0 <= j < N and table[j] == 'H' and not eat[j]:
                answer += 1
                eat[j] = True
                break

print(answer)
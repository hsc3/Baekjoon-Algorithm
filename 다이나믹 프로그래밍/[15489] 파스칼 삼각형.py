# [15489] 파스칼 삼각형 | Silver 4 | 다이나믹 프로그래밍
'''
파스칼 삼각형은 양 끝을 제외한 각 수는 자신의 바로 왼쪽 위의 수와 바로 오른쪽 위의 수의 합으로 되어있다.
이때 R번째 줄, C번째 수를 위 꼭짓점으로 하는 한 변이 포함하는 수의 개수가 W인 정삼각형과 그 내부를 생각하자. 정삼각형의 변과 그 내부에 있는 수들의 합을 구하고 싶다.
예를 들면, 3번 째 줄, 1번 째 수를 꼭짓점으로 하고 한 변이 포함하는 수의 개수가 4인 정삼각형과 그 내부에 있는 수의 합은 1+(1+3)+(1+4+6)+(1+5+10+10) = 42 이다.
주어진 R, C, W에 대해서 그에 해당하는 합을 구하는 프로그램을 작성하여라.
'''
import sys
input = sys.stdin.readline

R, C, W = map(int, input().split())
paskal = [[0 for _ in range(R+W-1)] for _ in range(R+W-1)]
paskal[0][0] = 1

# 파스칼 삼각형 생성
for i in range(1, R+W-1):
    paskal[i][0] = paskal[i-1][0]
    for j in range(1, R+W-1):
        paskal[i][j] = paskal[i-1][j-1] + paskal[i-1][j]

# 파스칼 삼각형에서 주어진 범위의 합 계산
answer = 0
cnt = 1
for i in range(R-1, R+W-1):
    answer += sum(paskal[i][C-1:C-1+cnt])
    cnt += 1

print(answer)
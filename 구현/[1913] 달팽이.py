# [1913] 달팽이 | Silver 3 | 구현
'''
홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.
N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오. 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오.
[입력] 첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.
'''
import sys
input = sys.stdin.readline

# 이동 방향 (북 동 남 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
K = int(input())
table = [[0 for _ in range(N)] for _ in range(N)]

move = [] # 이동 규칙
for i in range(1, N):
    move += [i, i]
move += [N]

x = N // 2
y = N // 2
i = 0 # 이동 방향
answer = []
num = 1

for m in move:
    while m: # 이동 규칙에 맞게 이동한다. (해당 방향으로 m칸 만큼 이동)
        table[x][y] = num
        if num == K:
            answer = [x+1, y+1]
        num += 1
        x += dx[i]
        y += dy[i]
        m -= 1
    i += 1 # m칸 이동하면 방향을 바꿔준다.
    if i == 4:
        i = 0


for i in range(N):
    print(*table[i])
print(*answer)
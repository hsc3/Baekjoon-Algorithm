'''
[1965] 상자넣기 / Silver 2 / 다이나믹 프로그래밍
정육면체 모양의 상자가 일렬로 늘어서 있다. 상자마다 크기가 주어져 있는데, 앞에 있는 상자의 크기가 뒤에 있는 상자의 크기보다 작으면, 앞에 있는 상자를 뒤에 있는 상자 안에 넣을 수가 있다.
상자의 크기가 주어질 때, 한 번에 넣을 수 있는 최대의 상자 개수를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

# 1. 이전의 계산 결과를 재사용 (똑같은 계산 x)
# 2. 현재 상자를 기준으로 다음으로 작은 상자의 결과값 + 1

n = int(input())

dp = [1] * n
box = list(map(int, input().split()))

for i in range(1, n) :
    for j in range(i) :
        if box[j] < box[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

'''
# 상자의 크기별로 dp 값을 저장

n = int(input())

dp = [0] * (1001)
boxes = list(map(int, input().split()))

for box in boxes:
    dp[box] = max(dp[:box]) + 1

print(max(dp))
'''

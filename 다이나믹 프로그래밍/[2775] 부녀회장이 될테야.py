# [2775] 부녀회장이 될테야
# Bronze 1 >> 동적 프로그래밍
'''
import sys
input = sys.stdin.readline

floor, roomNum = [], []

for _ in range(int(input())) :
    floor.append(int(input()))
    roomNum.append(int(input()))

maxFloor = max(floor)
maxRoomNum = max(roomNum)

dp = [[i for i in range(maxRoomNum+1)] for _ in range(maxFloor+1)]

for f in range(1,maxFloor+1) :
    for n in range(maxRoomNum+1) :
        dp[f][n] = sum(dp[f-1][:n+1])

    
for f, n in zip(floor, roomNum) :
    print(dp[f][n])
'''

import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    floor = int(input())
    roomNum = int(input())

    dp = [i for i in range(roomNum+1)]

    for _ in range(floor) :
        for i in range(1, roomNum+1) :
            dp[i] += dp[i-1]

    print(dp[roomNum])
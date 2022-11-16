# [25192] 인사성 밝은 곰곰이 | Silver 4 | https://www.acmicpc.net/problem/25192
import sys
input = sys.stdin.readline

answer = 0
N = int(input())
user = set()

for _ in range(N):
    data = input().rstrip()
    if data == "ENTER": # 새로운 사람이 들어오면, 곰곰이 이모티콘을 사용한 횟수 누적
        answer += len(user)
        user.clear()
    else: # 채팅을 친 유저를 한 번만 추가 (곰곰이 이모티콘을 사용한 횟수)
        user.add(data)
answer += len(user)
print(answer)

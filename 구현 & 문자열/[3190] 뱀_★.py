# Gold 5 [3190] 뱀 | 자료구조, 구현
import sys; input = sys.stdin.readline
from collections import deque

N = int(input()) 

# 사과의 위치 입력
apples = []
for _ in range(int(input())) :
    x, y = map(int, input().split())
    apples.append([x-1, y-1])
    
# 뱀의 방향 전환 횟수
direction_change = deque()
for _ in range(int(input())) :
    sec, direction = input().split()
    direction_change.append([int(sec), direction])

# 게임 구현 ========================================================================
# 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다 --> 게임이 몇 초에 끝나는지 계산하라.
direction = deque([[0,1], [1,0], [0,-1], [-1,0]]) # 머리의 이동 방향 →, ↓, ←, ↑
snake = deque([[0, 0]]) # 뱀이 차지하고 있는 좌표 [ 머리 <-> 꼬리 ]
second = 0 # 게임이 진행되는 시간

while True :
    # 1. 머리 이동
    next_head = [snake[0][0] + direction[0][0], snake[0][1] + direction[0][1]]
    second += 1

    # 2. 게임이 종료되는 경우인지 체크.
    if (not (0 <= next_head[0] < N and 0 <= next_head[1] < N)) or (next_head in snake) :
        break

    # 3. 뱀의 머리 방향 전환 체크.
    if len(direction_change) > 0 and second == direction_change[0][0] : # 방향을 전환해야하는 시간인 경우
        if direction_change[0][1] == 'L' :
            direction.rotate(1)
        else : # direction_change[0][1] == 'D'
            direction.rotate(-1)
        direction_change.popleft()
    snake.appendleft(next_head)

    # 4. 해당 위치에 사과가 존재하는 경우와 존재하지 않는 경우 체크
    if next_head in apples : # 사과가 존재하는 경우 -> 꼬리의 위치를 유지하고, 사과를 삭제한다.
        apples.remove(next_head)
    else : # 사과가 존재하지 않는 경우 -> 꼬리의 길이를 줄인다.
        snake.pop()

print(second)

'''
N = int(input()) 
board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1
# 사과의 위치 입력
for _ in range(int(input())) :
    x, y = map(int, input().split())
    board[x-1][y-1] = 2
    
# 뱀의 방향 전환 횟수
direction_change = deque()
for _ in range(int(input())) :
    sec, direction = input().split()
    direction_change.append([int(sec), direction])

# 게임 구현 ========================================================================
# 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다 --> 게임이 몇 초에 끝나는지 계산하라.
direction = deque([[0,1], [1,0], [0,-1], [-1,0]]) # 머리의 이동 방향 →, ↓, ←, ↑
head = [0,0]
tail = deque()
second = 0 # 게임이 진행되는 시간

while True :
    # 1. 머리 이동
    head[0] += direction[0][0]
    head[1] += direction[0][1]
    second += 1

    # 2. 게임이 종료되는 경우인지 체크.
    if (not (0 <= head[0] < N and 0 <= head[1] < N)) or (board[head[0]][head[1]] == 1) :
        break

    # 3. 뱀의 머리 방향 전환 체크.
    if len(direction_change) > 0 and second == direction_change[0][0] : # 방향을 전환해야하는 시간인 경우
        if direction_change[0][1] == 'L' :
            direction.rotate(1)
        else : # direction_change[0][1] == 'D'
            direction.rotate(-1)
        direction_change.popleft()

    # 4. 해당 위치에 사과가 존재하는 경우와 존재하지 않는 경우 체크
    if board[head[0]][head[1]] == 2 : # 사과가 존재하는 경우 -> 꼬리의 길이를 유지한다.
        tail.append(head)
    else : # 사과가 존재하지 않는 경우 -> 꼬리의 길이를 줄인다. 
        tail.popleft()
        board[tail[0]][tail[1]] = 0

    board[head[0]][head[1]] = 1

print(second)
'''
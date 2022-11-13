# [15828] Router | Silver 4 | https://www.acmicpc.net/problem/15828
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
buffer = deque()
buffer_size = 0
while True:
    packet = int(input())
    if packet == -1:
        break
    elif packet == 0:
        buffer.popleft()
        buffer_size -= 1
    elif buffer_size < N:
        buffer.append(packet)
        buffer_size += 1

if buffer:
    print(*buffer)
else:
    print("empty")

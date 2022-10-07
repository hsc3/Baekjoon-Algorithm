# [1094] 막대기 | Silver 5 | https://www.acmicpc.net/problem/1094
from heapq import heappush, heappop

def Solution(X):
    sticks = []
    heappush(sticks, 64)

    while sum(sticks) != X:
        shortest_stick = heappop(sticks) # 가장 짧은 막대
        if sum(sticks) + shortest_stick // 2 < X: # 절반으로 자른 막대의 길이 + 나머지 막대 길이가 X보다 작으면,
            heappush(sticks, shortest_stick // 2) # 자른 막대 2개를 모두 가지고 있는다.
        heappush(sticks, shortest_stick // 2) # X보다 길면, 자른 막대 중 하나를 버린다.

    return len(sticks)

if __name__ == "__main__":
    print(Solution(int(input())))
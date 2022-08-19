# [10971] 외판원 순회 (2) | Silver 2 | 백트랙킹, 브루트포스
'''
1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다) 이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외)
이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.
각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다.
모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다. 경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.
N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def TSP(start, cost, visited):
    global answer

    if False not in visited[1:]:
        if W[start][0] != 0:
            answer = min(answer, cost + W[start][0])
        return

    for destination in range(1, N):
        
        # [방문 조건]
        # 1. start -> destination 의 경로가 존재하는 경우
        # 2. destination을 아직 방문하지 않은 경우
        # 3. 최소 비용의 경로일 수 있는 경우 (지금까지 최소 비용을 넘지 않은 경로인 경우)
        if W[start][destination] != 0 and not visited[destination] and cost + W[start][destination] < answer:

            visited[destination] = True # 방문
            TSP(destination, cost + W[start][destination], visited)
            visited[destination] = False # 미방문

if __name__ == "__main__":
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]

    answer = float("inf")
    TSP(0, 0, [False for _ in range(N)])

    print(answer)
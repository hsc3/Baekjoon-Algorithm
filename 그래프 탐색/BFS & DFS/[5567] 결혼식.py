# [5567] 결혼식 | Silver 2 | 그래프
'''
상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다. 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.
상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

# DFS - stack
def DFS(stk, depth):
    global answer

    if len(stk) == 0 or depth >= 2: # 스택이 비었거나, 친구의 친구의 관계를 넘어서는 경우 종료
        return

    me = stk.pop(0)
    for friend in graph[me]:
        if not visited[friend]: # 아직 초대하지 않은 친구인 경우
            visited[friend] = True # 초대를 하고
            answer += 1 # 초대할 사람의 수를 1 증가
        DFS(stk + [friend], depth + 1) # 다음 친구를 탐색합니다.




if __name__ == "__main__":
    n = int(input()) # 동기의 수
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    visited[1] = True

    for _ in range(int(input())):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = 0
    DFS([1], 0)
    print(answer)
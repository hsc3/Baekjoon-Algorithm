'''
[2606] 바이러스 | Silver 3 | 그래프 (BFS)
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크 수
adj = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m) :
    s, e = map(int, input().split())
    adj[e].append(s)
    adj[s].append(e)

q = [1]
cnt = 0
while q :
    v = q.pop(0)
    if visited[v] == False :
        visited[v] = True
        cnt += 1
        for a in adj[v] :
            if visited[a] == False :
                q.append(a)

print(cnt-1)

'''
[1012] 유기농 배추  | Silver 2 | 그래프
배추를 군데군데 심어 놓았다. 배추흰지렁이는 인접해있는 배추를 옮겨다니며 보호할 수 있다. 
배추를 보호하기 위해서 총 몇 마리의 지렁이가 필요한지 조사하시오.
'''
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

t = int(input()) # 테스트 케이스
res = []
for _ in range(t) :
    n, m, k = map(int, input().split()) # 가로, 세로, 배추의 개수
    l = [[0 for _ in range(m)] for _ in range(n)]
    baechu = []
    cnt = 0
    # 배추의 위치 구성
    for _ in range(k) :
        x, y = map(int, input().split())
        l[x][y] = 1
        baechu.append([x,y])

    for b in baechu :
        if l[b[0]][b[1]] == 1 : # 배추가 심어진 위치인 경우
            q = [[b[0],b[1]]]
            while q :
                x, y = map(int, q.pop(0))
                if l[x][y] == 1 :
                    l[x][y] = 0 # 인접한 배추를 한 마라의 지렁이가 보호합니다. (배추가 없는 것으로 설정)
                    for i in range(4) :
                        xx = x + dx[i]
                        yy = y + dy[i]
                        if 0 <= xx < n and 0 <= yy < m and l[xx][yy] == 1 :
                            q.append([xx,yy])
            cnt += 1 # 인접해있는 배추의 구역을 카운트 합니다. (필요한 지렁이의 수 카운트)
    res.append(cnt)

print(*res, sep = '\n')


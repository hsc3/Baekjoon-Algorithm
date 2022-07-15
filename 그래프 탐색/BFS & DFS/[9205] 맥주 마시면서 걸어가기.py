'''
[9205] 맥주 마시면서 걸어가기 / Silver 1 / 그래프 탐색
송도에 사는 상근이와 친구들은 송도에서 열리는 펜타포트 락 페스티벌에 가려고 한다. 올해는 맥주를 마시면서 걸어가기로 했다. 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다.
맥주 한 박스에는 맥주가 20개 들어있다. 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다. 즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.
상근이의 집에서 페스티벌이 열리는 곳은 매우 먼 거리이다. 따라서, 맥주를 더 구매해야 할 수도 있다. 미리 인터넷으로 조사를 해보니 다행히도 맥주를 파는 편의점이 있다.
편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다. 하지만, 박스에 들어있는 맥주는 20병을 넘을 수 없다. 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.
편의점, 상근이네 집, 펜타포트 락 페스티벌의 좌표가 주어진다. 상근이와 친구들이 행복하게 페스티벌에 도착할 수 있는지 구하는 프로그램을 작성하시오.
(두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. (맨해튼 거리))
각 테스트 케이스에 대해서 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 "happy", 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"를 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

answer =  []
for _ in range(int(input())): # test case
    n = int(input()) # 편의점 갯수
    store = [] # 편의점의 좌표 저장
    possibility = False # 맥주를 마시면서 페스티벌에 도착할 수 있는지 여부

    home = list(map(int, input().split()))
    for _ in range(n):
        store.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))

    locations = store + [festival] # 들릴 수 있는 장소들
    visited = [False] * len(locations) # 들렸는지 여부를 체크

    queue = deque([home])
    while queue:
        x, y = map(int, queue.popleft())
        for i in range(len(locations)):
            if not visited[i] and abs(locations[i][0] - x) + abs(locations[i][1] - y) <= 1000: # 들릴 수 있는 경우
                visited[i] = True
                if locations[i] == festival: # 들린 곳이 최종 도착지일 경우, 종료
                    possibility = True
                    break
                queue.append(locations[i])
    answer.append("happy") if possibility else answer.append("sad")

print(*answer, sep='\n')


'''
[2346] 풍선 터뜨리기 / Silver 3 / 자료구조(덱)
1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고. i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다. 
단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다. 각 풍선 안에는 종이가 하나 들어있고, 
종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다. 이 풍선들을 다음과 같은 규칙으로 터뜨린다.
- 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 
  다음 풍선을 터뜨린다. 
- 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 이미 터진 풍선은 빼고 이동한다.
첫째 줄에 터진 풍선의 번호를 차례로 나열하는 프로그램을 작성하라.
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())
balloons = deque(enumerate(map(int, input().split())))
#num_in_balloons = list(map(int, input().split()))
#balloons = deque([i, num_in_balloons[i-1]] for i in range(1, N+1)) 
res = []

while balloons :
    balloon = balloons.popleft()
    res.append(balloon[0]+1)
    if balloon[1] > 0 : 
        balloons.rotate(-(balloon[1]-1)) # left rotation 수행
    else : 
        balloons.rotate(-balloon[1]) # right rotation 수행

print(*res)
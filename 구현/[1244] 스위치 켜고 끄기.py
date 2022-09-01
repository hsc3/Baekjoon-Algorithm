# [1244] 스위치 켜고 끄기 | Silver 4 | 구현
'''
1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다. ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다.
그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다.
학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.
- 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
- 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
입력으로 스위치들의 처음 상태가 주어지고, 각 학생의 성별과 받은 수가 주어진다. 학생들은 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때, 스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.

출력 : 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다. 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다. 켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 둔다.
'''
import sys
input = sys.stdin.readline

def Man(loc): # loc의 배수에 해당하는 스위치 변경
    for i in range(loc, N, loc+1):
        switch[i] = abs(switch[i] - 1)

def Woman(loc): # loc 기준, 좌우로 대칭을 이루는 최대 구간 스위치 변경
    # 1. 대칭을 이루는 폭 너비를 구한다.
    same_width = 0 # 대칭을 이루는 폭의 너비
    while True:
        same_width += 1
        if loc - same_width < 0 or N <= loc + same_width: # 스위치 구간의 양끝에 도달한 경우 종료
            break
        left = switch[loc - same_width]  # 대칭을 이루는 왼쪽 스위치
        right = switch[loc + same_width]  # 대칭을 이루는 오른쪽 스위치
        if left != right: # 좌우 스위치가 대칭을 이루지 않는 경우 종료
            break

    # 2. 폭 너비만큼 양쪽으로 스위치를 변경한다.
    switch[loc] = abs(switch[loc] - 1)
    for i in range(1, same_width):
        switch[loc - i] = abs(switch[loc - i] - 1)
        switch[loc + i] = abs(switch[loc + i] - 1)

if __name__=="__main__":
    N = int(input()) # 스위치의 갯수
    switch = list(map(int, input().split()))

    for _ in range(int(input())):
        gender, loc = map(int, input().split())
        Man(loc-1) if gender == 1 else Woman(loc-1)

    for i in range(len(switch)):
        if i > 0 and i % 20 == 0:
            print()
        print(switch[i], end=' ')
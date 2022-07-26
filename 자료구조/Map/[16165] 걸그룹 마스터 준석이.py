# [16165] 걸그룹 마스터 준석이 / Silver 3 / 자료구조(map)
'''
정우는 소문난 걸그룹 덕후이다. 정우의 친구 준석이도 걸그룹을 좋아하지만 이름을 잘 외우지 못한다는 문제가 있었다.
정우는 친구를 위해 걸그룹 개인과 팀의 이름을 검색하여 외우게 하는 퀴즈 프로그램을 만들고자 한다.
각각의 퀴즈는 두 줄로 이루어져 있으며, 팀의 이름이나 멤버의 이름이 첫 줄에 주어지고 퀴즈의 종류를 나타내는 0 또는 1이 두 번째 줄에 주어진다.
퀴즈의 종류가 0일 경우 팀의 이름이 주어지며, 1일 경우 멤버의 이름이 주어진다.
'''
import sys
input = sys.stdin.readline

girlGroup = dict()
N, M = map(int, input().split()) # 걸그룹의 수, 맞혀야할 문제의 수
for _ in range(N):
    groupName = input().rstrip()
    member = sorted([input().rstrip() for _ in range(int(input()))])
    girlGroup[groupName] = member

for _ in range(M):
    name = input().rstrip()
    quiz = int(input())
    if quiz == 0: # 걸그룹의 모든 멤버 출력
        print(*girlGroup[name], sep='\n')
    else: # 멤버가 속한 걸그룹 출력
        for groupName in girlGroup.keys():
            if name in girlGroup[groupName]:
                print(groupName)
                break

        

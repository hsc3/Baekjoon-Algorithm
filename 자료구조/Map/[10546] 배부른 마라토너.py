# [10546] 배부른 마라토너 / Silver 4 / 자료구조(map)
'''
마라토너라면 국적과 나이를 불문하고 누구나 참가하고 싶어하는 백준 마라톤 대회가 열린다. 42.195km를 달리는 이 마라톤은 모두가 참가하고 싶어했던 만큼 매년 모두가 완주해왔다. 단, 한 명만 빼고!
모두가 참가하고 싶어서 안달인데 이런 백준 마라톤 대회에 참가해 놓고 완주하지 못한 배부른 참가자 한 명은 누굴까?
'''
import sys
input = sys.stdin.readline

N = int(input())
runner = dict()
for _ in range(N): # 마라톤 참가자 입력
    name = input().rstrip()
    runner[name] = runner.get(name, 0) + 1
    
for _ in range(N-1): # 마라톤 완주자 입력
    name = input().rstrip()
    runner[name] -= 1

for key, value in runner.items():
    if value > 0:
        print(key)
        break
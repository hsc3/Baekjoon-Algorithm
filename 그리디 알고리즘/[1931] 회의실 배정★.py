'''
[1931] 회의실 배정 / Silver 1 / 그리디, 정렬
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작 시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작 시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''
import sys
input = sys.stdin.readline

seminaList = []
for _ in range(int(input())) :
    seminaList.append(list(map(int, input().split())))

seminaList.sort(key = lambda x : (x[1], x[1]-x[0])) # 회의의 끝나는 시간과 (끝나는 시간 - 시작 시간) 기준 오름차순 정렬

res = 1
begin, end = map(int, seminaList.pop(0))
for semina in seminaList :
    if semina[1] <= begin or semina[0] >= end : # 이전 세미나와 겹치지 않는 시간인 경우
        begin, end = semina[0], semina[1]
        res += 1

print(res)
# [11000] 강의실 배정 | Gold 5 | 그리디 알고리즘, 힙
'''
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.
김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
강의실의 개수를 출력하라.
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

seminar = []
# 가장 빨리 시작하고, 수업 시간이 짧은 수업을 선택한다.
N = int(input())
for _ in range(N):
    seminar.append(list(map(int, input().split())))

seminar.sort(key=lambda x : (x[0], x[1] - x[0]))
room = [] # 강의실 별 수업이 끝나는 시간을 저장

heappush(room, seminar[0][1]) # 첫 번째 강의의 끝나는 시간을 추가한다.
for i in range(1, N):
    if room[0] <= seminar[i][0]: # 해당 강의실에서 강의를 진행할 수 있는 경우 (가장 빨리 끝나는 강의실 시간 <= i번째 강의 시작 시간)
        heappop(room) # 기존 강의의 끝나는 시간을 꺼낸다. (강의실 - 1)
    heappush(room, seminar[i][1]) # i번째 수업 끝나는 시간을 추가한다. (강의실 + 1)

print(len(room))
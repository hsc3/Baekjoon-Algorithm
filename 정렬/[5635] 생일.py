'''
[5635] 생일 / Silver 5 / 정렬, 문자열
어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

birthday = dict()
for _ in range(int(input())) :
    inputData = list(input().split())
    birthday[inputData[0]] = birthday.get(inputData[0], list(map(int, inputData[1:])))

# 년, 월, 일 기준 오름차순 정렬 -> birthday에는 딕셔너리의 키 값만 저장되고, 리스트 형태로 반환된다.
birthday = sorted(birthday, key = lambda x : (birthday[x][2], birthday[x][1], birthday[x][0]))

print(birthday[-1], birthday[0], sep='\n')
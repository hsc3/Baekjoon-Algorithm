'''
[7785] 회사에 있는 사람 | Silver 5 | 자료구조 (Set)
Q : 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.
'''
N = int(input()) # 로그의 출입 기록 수
enter = set()
for _ in range(N) :
    name, entrance = input().split()
    if entrance == "enter" :
        enter.add(name)
    elif entrance == "leave" :
        enter.discard(name)

print(*sorted(enter, reverse = True), sep = '\n')

'''
from sys import stdin
input = lambda: stdin.readline().strip()

person = dict()
n = int(input())
for i in range(n):
    name, command = input().split()
    if command == 'enter':
        person[name] = True
    else:
        del person[name]

for i in sorted(person.keys(), reverse=True):
    print(i)
'''
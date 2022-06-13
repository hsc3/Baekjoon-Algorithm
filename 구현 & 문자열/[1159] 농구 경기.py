'''
[1159] 농구 경기 | 구현, 문자열
상근이는 내일 경기에 나설 선발 명단을 작성해야 한다.
따라서, 누가 선발인지 기억하기 쉽게 하기 위해 성의 첫 글자가 같은 선수 5명을 선발하려고 한다. 
만약, 성의 첫 글자가 같은 선수가 5명보다 적다면, 상근이는 내일 있을 친선 경기를 기권하려고 한다.
상근이는 내일 경기를 위해 뽑을 수 있는 성의 첫 글자를 모두 구해보려고 한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
d = dict()

for _ in range(n) :
    name = input().rstrip()
    d[name[0]] = d.get(name[0], 0) + 1

answer = []
for name, count in d.items() :
    if count >= 5 :
        answer.append(name)

answer.sort()
if len(answer) == 0 :
    print("PREDAJA") 
else :
    print(*answer, sep = '')
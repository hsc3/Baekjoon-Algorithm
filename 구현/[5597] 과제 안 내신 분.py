'''
[5597] 과제 안 내신 분..? / Bronze 5 / 구현
X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.
'''

import sys 
input = sys.stdin.readline

check = [i for i in range(1, 31)]
for _ in range(28) :
    check.remove(int(input()))
print(*check, sep = '\n')

'''
check = [False] * 30
res = []

for _ in range(28) :
    check[int(input())-1] = True

for i in range(30) :
    if check[i] == False :
        res.append(i+1)

print(*res, sep='\n')
'''
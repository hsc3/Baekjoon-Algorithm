'''
[8958] OX퀴즈 / Bronze 2 / 구현, 문자열
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
예를 들어, 10번 문제의 점수는 3이 된다. "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

res = []

for _ in range(int(input())):
    quiz = input().rstrip()
    tmp = 0
    score = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            tmp += 1
            score += tmp
        else: 
            tmp = 0
    res.append(score)

print(*res, sep = '\n')
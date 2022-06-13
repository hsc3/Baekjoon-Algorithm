# [8958] OX퀴즈
# Bronze 2 >> 구현, 문자열

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
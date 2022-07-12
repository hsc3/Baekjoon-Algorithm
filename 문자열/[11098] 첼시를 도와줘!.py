'''
[11098] 첼시를 도와줘! / Bronze 2 / 문자열
현재 첼시는 프리미어 리그에서 헤매고 있고, 결국 새로운 선수를 사기로 결정했다. 하지만 그들은 스카우터를 기다리기 지쳤고, 훨씬 더 효율적인 전략을 개발해냈다.
"만약 무언가 팔리고 있다면, 그것에는 합당한 이유가 있다"는 배룸의 명언이 바로 그것이다. 축구에서 이 말은 곧 가장 비싼 선수가 가장 좋은 선수라는 이야기가 된다.
이에 따라 새로운 선수를 찾는 방법은 단순히 구단들에게 전화를 걸어 그들의 가장 비싼 선수를 사는게 되었다.
당신의 임무는 첼시가 리스트에서 가장 비싼 선수를 찾아낼 수 있도록 돕는 것이다.
'''

import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    maxValue = 0  # 가장 비싼 선수의 몸값
    valuablePlayer = '' # 영입할 선수
    for _ in range(int(input())):
        value, player = input().split()
        if maxValue < int(value):
            maxValue = int(value)
            valuablePlayer = player

    answer.append(valuablePlayer)

print(*answer, sep = '\n')
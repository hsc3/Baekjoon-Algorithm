'''
[1544] 사이클 단어 / Silver 4 / 자료구조(덱), 문자열
사이클 단어는 어떤 단어를 원형 모양으로 차례대로 쓴 것이다.
따라서, 어떤 단어를 이렇게 쓴 후에 임의의 단어를 고른다. 그 후에 시계방향으로 차례대로 읽으면 그 것이 단어가 된다.
만약에 단어 A와 단어 B가 있을 때, 단어 B를 원형으로 써서, 단어 A와 같이 읽을 수 있으면, 두 단어는 같은 단어이다.
따라서, picture와 turepic은 같은 단어다.
N개의 단어가 주어졌을 때, 서로 다른 단어가 총 몇 개인지 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
words = [input().rstrip() for _ in range(N)]
i = 0
while True :
    if i == len(words) :
        break
    word = deque(w for w in words[i])

    # 해당 단어를 rotate해서 만들 수 있는 모든 단어 생성
    rotatedWords = []
    for _ in range(len(word)) :
        word.rotate(1)
        rotatedWords.append(''.join(word))

    j = i+1
    while True :
        if j == len(words) :
            break

        if words[j] in rotatedWords : # 사이클 단어 제거
            words.pop(j)
        else :
            j += 1
    i += 1

print(len(words))
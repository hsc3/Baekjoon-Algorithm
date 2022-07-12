'''
[5218] 알파벳 거리 / Bronze 2 / 문자열
길이가 같은 두 단어가 주어졌을 때, 각 단어에 포함된 모든 글자의 알파벳 거리를 구하는 프로그램을 작성하시오.
두 글자 x와 y 사이의 알파벳 거리를 구하려면, 먼저 각 알파벳에 숫자를 할당해야 한다.
'A'=1, 'B' = 2, ..., 'Z' = 26. 그 다음 y ≥ x인 경우에는 y-x, y < x인 경우에는 (y+26) - x가 알파벳 거리가 된다.
예를 들어, 'B'와 'D' 사이의 거리는 4 - 2 = 2이고, 'D'와 'B' 사이의 거리는 (2+26) - 4 = 24이다.
'''
import sys
input = sys.stdin.readline

answer = []
T = int(input())
for _ in range(T):
    strA, strB = map(str, input().split())
    length = len(strB)

    distance = []
    for i in range(length):
        distCharA = ord(strA[i])
        distCharB = ord(strB[i])
        distDifference = distCharB - distCharA # 두 알파벳의 거리 계산
        if distDifference >= 0:
            distance.append(str(distDifference))
        else:
            distance.append(str(26+distDifference))
    answer.append("Distances: {}".format(' '.join(distance)))

print(*answer, sep='\n')
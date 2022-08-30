# [1969] DNA | Silver 5 | 문자열
'''
DNA는 서로 다른 4가지의 뉴클레오티드로 이루어져 있다(Adenine, Thymine, Guanine, Cytosine).
우리는 어떤 DNA의 물질을 표현할 때, 이 DNA를 이루는 뉴클레오티드의 첫글자를 따서 표현한다.
그리고 Hamming Distance란 길이가 같은 두 DNA가 있을 때, 각 위치의 뉴클오티드 문자가 다른 것의 개수이다.
만약에 “AGCAT"와 ”GGAAT"는 첫 번째 글자와 세 번째 글자가 다르므로 Hamming Distance는 2이다.
우리가 할 일은 다음과 같다. N개의 길이 M인 DNA s1, s2, ..., sn가 주어져 있을 때 Hamming Distance의 합이 가장 작은 DNA s를 구하는 것이다.
즉, s와 s1의 Hamming Distance + s와 s2의 Hamming Distance + s와 s3의 Hamming Distance ... 의 합이 최소가 된다는 의미이다.
'''
import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split()) # DNA의 갯수, 문자열의 길이
DNA = [input().rstrip() for _ in range(N)]

my_DNA = ""
for column in list(zip(*DNA)): # (입력받은 기존 DNA 배열의 row와 column을 변환)
    # most_common(1)[0][0] -> 입력받은 DNA들의 각 자리에서 가장 빈번한 알파벳 저장
    # sorted -> 동일 횟수로 나타나는 알파벳이 있는 경우, 사전순 가장 빠른 알파벳 선택
    my_DNA += Counter(sorted(column)).most_common(1)[0][0]

hamming_distance = 0
for i in range(N): # 입력받은 i번째 DNA와 구한 DNA의 hamming distance 계산
    for j in range(M):
        if my_DNA[j] != DNA[i][j]:
            hamming_distance += 1

print(my_DNA)
print(hamming_distance)
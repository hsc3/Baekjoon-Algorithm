# [11652] 카드 | Silver 4 | 자료구조(map)
'''
준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -26^2보다 크거나 같고, 26^2보다 작거나 같다.
준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러가지 라면, 작은 것을 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
map = {}
for _ in range(N) :
    num = int(input())
    map[num] = map.get(num, 0) + 1 # 해당 key의 value값 반환 (0는 default값 : key가 존재하지 않을 경우)
max_value = max(map.values())
max_key = [x for x, y in map.items() if y == max_value]
print(min(max_key))

'''
from collections import Counter
N = int(input())
cards = [int(input()) for _ in range(N)]
cards_count = dict(Counter(cards))
print(sorted(cards_count, key = lambda x : (-cards_count[x], x))[0])
'''    
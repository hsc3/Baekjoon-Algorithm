'''
[2910] 빈도 정렬 / Silver 3 / 정렬, 구현
메시지는 숫자 N개로 이루어진 수열이고, 숫자는 모두 C보다 작거나 같다. 이 숫자를 자주 등장하는 빈도순 대로 정렬하려고 한다.
수열의 두 수 X와 Y가 있을 때, X가 Y보다 수열에서 많이 등장하는 경우에는 X가 Y보다 앞에 있어야 한다.
만약, 등장하는 횟수가 같다면, 먼저 나온 것이 앞에 있어야 한다. 이렇게 정렬하는 방법을 빈도 정렬이라고 한다.
수열이 주어졌을 때, 빈도 정렬을 하는 프로그램을 작성하시오.
'''
from collections import Counter
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
msg = list(map(int, input().split()))
counter = sorted(list(Counter(msg).items()), key = lambda x : -x[1]) # 빈도 순 정렬

for num, frequency in counter :
    print(*[num for _ in range(frequency)], end = ' ')
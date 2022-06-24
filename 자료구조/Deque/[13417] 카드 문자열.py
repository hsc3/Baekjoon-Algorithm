'''
[13417] 카드 문자열 / Silver 4 / 자료구조(덱), 문자열
N장의 카드가 일렬로 놓여있다. 각 카드에는 알파벳이 하나씩 적혀있다. 태욱이는 가장 왼쪽에 있는 카드부터 차례대로 한 장씩 가져올 수 있다.
가장 처음에 가져온 카드는 자신의 앞에 놓는다. 그 다음부터는 가져온 카드를 자신의 앞에 놓인 카드들의 가장 왼쪽, 또는 가장 오른쪽에 놓는다.
태욱이는 모든 카드를 다 가져온 후에 자신의 앞에 놓인 카드를 순서대로 이어 붙여 카드 문자열을 만들려고 한다.
N장의 카드에 적혀있는 알파벳의 처음 순서가 주어질 때, 태욱이가 만들 수 있는 카드 문자열 중 사전 순으로 가장 빠른 문자열을 출력하는 프로그램을 작성하시오.
'''
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
res = []

for _ in range(T) :
    N = int(input())
    cards = list(input().split())
    my_card = deque()

    for i in range(len(cards)) :
        if i == 0 :
            my_card.append(cards[i])
        else :
            if cards[i] <= my_card[0] :
                my_card.appendleft(cards[i])
            else :
                my_card.append(cards[i])
    res.append(''.join(my_card))

print(*res, sep = '\n')
'''
[2164] 카드2 / Silver 4 / 자료구조(큐)
각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다. 
이를 반복했을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
'''

# 큐를 활용할 경우, 규칙성을 파악해야 한다.
# [1,2,3,4,5] -> [5,2,4] 
# [1,2,3,4,5,6] -> [6,2,4]
# [1,2,3,4,5,6,7] -> [7,2,4,6]

cards = [i for i in range(1, int(input())+1)]

while len(cards) > 1 :
    if len(cards) % 2 == 1 :
        tmp = [cards[-1]]
        tmp.extend(cards[1::2])
        cards = tmp
    else : 
        cards = cards[1::2]

print(cards[0])

'''
from collections import deque

cards = deque(i for i in range(1, int(input())+1))

while len(cards) > 1 :
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
'''

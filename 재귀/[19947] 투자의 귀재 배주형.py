# [19947] 투자의 귀재 배주형 | Silver 5 | 재귀
'''
주형이가 하려는 투자에는 3가지 방법의 투자 방식이 있다.
- 1년마다 5%의 이율을 얻는 투자 (A)
- 3년마다 20%의 이율을 얻는 투자 (B)
- 5년마다 35%의 이율을 얻는 투자 (C)

투자를 할 때에는 다음과 같은 주의점이 있다.
- 투자의 기한(1년, 3년, 5년)을 채우는 시점에 이율이 반영되며, 그 사이에는 돈이 늘어나지 않는다.
- 투자 방식은 매년 바꿀 수 있다.
- 매번 이율은 소수점 이하를 버림 해서 받는다.

예를 들어서, 지금 가진 돈이 11111원이면, A 방식이면 1년 후에 555원, B 방식이면 3년 후에 2,222원, C 방식이면 5년 후에 3,888원을 이자로 받을 수 있다. 만약 C 방식으로 투자했지만 4년이 지난 시점이라면 받을 수 있는 이자는 0원이다.
주형이의 초기 비용이 H원일 때, Y년이 지난 시점에 가장 많은 금액을 얻을 수 있는 투자 패턴을 분석하고 그 금액을 출력하자.
'''
from math import floor

def Investment(year, money):
    global answer

    if year >= Y:
        if year == Y: # 투자 가능한 패턴인 경우에만 최대 금액을 갱신
            answer = max(answer, money)
        return

    Investment(year+1, floor(money*1.05)) # 1년 적금
    Investment(year+3, floor(money*1.20)) # 3년 적금
    Investment(year+5, floor(money*1.35)) # 5년 적금


if __name__ == "__main__":
    H, Y = map(int, input().split()) # 투자 비용, 투자 기간
    answer = 0 # 최대 금액

    Investment(0, H);
    print(answer)
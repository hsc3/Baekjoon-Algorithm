# [11501] 주식 | Silver 2 | 그리디
'''
홍준이는 요즘 주식에 빠져있다. 그는 미래를 내다보는 눈이 뛰어나, 날 별로 주가를 예상하고 언제나 그게 맞아떨어진다. 매일 그는 아래 세 가지 중 한 행동을 한다.
- 주식 하나를 산다.
- 원하는 만큼 가지고 있는 주식을 판다.
- 아무것도 안한다.
홍준이는 미래를 예상하는 뛰어난 안목을 가졌지만, 어떻게 해야 자신이 최대 이익을 얻을 수 있는지 모른다. 따라서 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.
예를 들어 날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다. 그러나 만약 날 별로 주가가 3, 5, 9일 때는 처음 두 날에 주식을 하나씩 사고, 마지막날 다 팔아 버리면 이익이 10이 된다.
'''
import sys
input = sys.stdin.readline

def Simulator(N, stock):
    profit = 0  # 총 이익

    highest_price = stock[N - 1]  # 최대 주가
    cursor = N - 2  # 주식을 사는 시점

    while cursor >= 0:
        # 더 높은 주가를 기록하는 날이 있는 경우 -> 최대 주가를 갱신
        if stock[cursor] > highest_price:
            highest_price = stock[cursor]
        # highest_price가 가장 높은 주가인 경우 -> 해당 주가를 가지고 cursor 시점의 이익을 계산
        else:
            profit += (highest_price - stock[cursor])
        cursor -= 1
    return profit

answer = []
for _ in range(int(input())):
    N = int(input())
    stock = list(map(int, input().split()))
    answer.append(Simulator(N, stock))

print(*answer, sep='\n')

# def Simulator(N, stock):
#     profit = 0
#
#     for day in range(N-1):
#         highest_price = max(stock[day+1:]) # 이후의 주식의 최대가
#         if stock[day] < highest_price: # 이 날(day) 주식을 사면, 이득을 볼 수 있는 경우
#             print("{}일 기준 최대 주가는 {}이고, 그로 인한 수익은 {}입니다.".format(day+1, highest_price, highest_price-stock[day]))
#             profit += (highest_price - stock[day]) # 최대가일 때, 해당 주식을 팔아 수익을 본다.
#         else:
#             print("{}일 기준으로 수익을 볼 수 없으므로, 주식을 사지 않습니다.".format(day+1))
#     return profit
#
# answer = []
# for _ in range(int(input())):
#     N = int(input())
#     stock = list(map(int, input().split()))
#
#     answer.append(Simulator(N, stock))
#
# print(*answer, sep='\n')

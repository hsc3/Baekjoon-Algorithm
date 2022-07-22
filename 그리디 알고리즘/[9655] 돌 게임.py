# [9655] 돌 게임 / Silver 5/ 그리디 알고리즘
'''
돌 게임은 두 명이서 즐기는 재밌는 게임이다.
탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.
두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.
'''
def recursion(turn, n) :
    if n > 3 : # 돌이 4개 이상 있으면 3개를 가져간다.
        return recursion(turn + 1, n - 3)
    elif n > 1 : # 돌이 3개보다 적고 마지막 돌은 아닌 경우, 1개를 가져간다.
        return recursion(turn + 1, n - 1)
    return turn # 마지막 돌을 가져간 경우, 종료

n = int(input())
result = recursion(0, n)
if result % 2 == 0 :
    print("SK")
else :
    print("CY")
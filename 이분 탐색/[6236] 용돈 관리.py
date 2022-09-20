# [6236] 용돈 관리 | Silver 2 | 이분 탐색
'''
현우는 용돈을 효율적으로 활용하기 위해 계획을 짜기로 하였다. 현우는 앞으로 N일 동안 자신이 사용할 금액을 계산하였고, 돈을 펑펑 쓰지 않기 위해 정확히 M번만 통장에서 돈을 빼서 쓰기로 하였다.
현우는 통장에서 K원을 인출하며, 통장에서 뺀 돈으로 하루를 보낼 수 있으면 그대로 사용하고, 모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원을 인출한다.
다만 현우는 M이라는 숫자를 좋아하기 때문에, 정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다.
현우는 돈을 아끼기 위해 인출 금액 K를 최소화하기로 하였다. 현우가 필요한 최소 금액 K를 계산하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def SpendSimulator(budget) : # 인출 횟수 계산
    cnt = 1 # 인출 횟수
    remainMoney = budget # 사용하고 남은 돈
    for i in range(N):
        if remainMoney < money[i]: # 인출을 해야만 하는 경우
            remainMoney = budget - money[i]
            cnt += 1
        else: # 인출을 하지 않아도 되는 경우
            remainMoney -= money[i]

    return cnt

if __name__ == "__main__":
    N, M = map(int, input().split()) # 사용 횟수, 인출 횟수
    money = [int(input()) for _ in range(N)]

    start = max(money)
    end = sum(money)
    answer = 0
    while start <= end:
        mid = (start + end) // 2 # 인출 금액
        cnt = SpendSimulator(mid)
        if cnt <= M: # 목표 인출 횟수보다 적거나 같은 경우 -> 더 적은 인출 금액을 탐색
            answer = mid
            end = mid - 1
        else: # 목표 인출 횟수보다 큰 경우 -> 더 큰 인출 금액을 탐색
            start = mid + 1

    print(answer)

'''
from sys import stdin

input = stdin.readline

def main():
    N, M = map(int, input().split())
    daily = [int(input()) for _ in range(N)]

    start = max(daily)
    end = sum(daily)
    ans = 0
    while start <= end:
        mid = (start + end) // 2

        current = mid
        count = 1
        for day in daily:
            if current < day:
                current = mid
                count += 1
            current -= day

        if count <= M:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    print(ans)

if __name__ == "__main__":
    main()
'''
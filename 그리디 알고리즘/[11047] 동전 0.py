'''
[11047] 동전 0 / Silver 4 / 그리디 알고리즘
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse = True)

res = 0
# 큰 금액의 동전부터 금액을 차감한다.
while K :
    for coin in coins : 
        if K // coin : 
            res += (K // coin)
            K %= coin

print(res) 
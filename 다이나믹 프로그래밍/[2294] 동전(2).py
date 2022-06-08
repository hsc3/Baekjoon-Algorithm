'''
[2294] 동전 2  |  https://www.acmicpc.net/problem/2294
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다.
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.
'''
N, K = map(int, input().split())
coin = []
for _ in range(N) :
    coin.append(int(input()))
dp = [float("inf") for _ in range(K+1)]
dp[0] = 0
res = 0
coin.sort(reverse = True)
for c in coin :
    for i in range(1,K+1) :
        if i - c >= 0 :
            dp[i] = min(dp[i], dp[i-c] + 1)

if dp[K] == float("inf") :
    print(-1)
else :
    print(dp[K])
# print(-1 if dp[-1] == 10001 else dp[-1])
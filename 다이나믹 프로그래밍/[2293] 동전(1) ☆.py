'''
[2293] 동전 1 / Gold 5 / 다이나믹 프로그래밍
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 
그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다. 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
'''
N, K = map(int, input().split()) # 동전의 갯수, 가치의 합
coin = []
for _ in range(N) :
    coin.append(int(input()))
    
dp = [0 for _ in range(K+1)]
dp[0] = 1

for c in coin : # c = [1,2,5] 
    for i in range(1,K+1) :
        if i - c >= 0 :
            dp[i] += dp[i-c] # 금액의 차 만큼을 건너뛴다.
print(dp[K])

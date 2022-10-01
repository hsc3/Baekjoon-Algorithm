# [12865] 평범한 배낭 | Gold 5 | https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())
things = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)] # [물건의 무게, 가치]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)] # i번째 물건까지 담았을 때의 최대 가치

for i in range(1, N+1): 
    for j in range(1, K+1):

        if j - things[i][0] >= 0: # i번째 물건을 담을 수 있는 경우, 최대 가치 갱신
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - things[i][0]] + things[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])

'''
def Knapsack(i, weight, value):
    global answer
    if i == N:
        answer = max(answer, value)
        return

    if weight + things[i][0] <= K: # 물건을 담는 경우
        Knapsack(i+1, weight + things[i][0], value + things[i][1])

    Knapsack(i+1, weight, value) # 물건을 담지 않는 경우

if __name__ == "__main__":
    N, K = map(int, input().split())
    things = [list(map(int, input().split())) for _ in range(N)] # [무게, 가치]
    answer = 0
    Knapsack(0, 0, 0)
    print(answer)
'''
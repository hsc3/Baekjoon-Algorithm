'''
[1535] 안녕 / Silver 2 / 다이나믹 프로그래밍 
세준이를 생각해준 사람은 총 N명이 있다. 사람의 번호는 1번부터 N번까지 있다. 
세준이가 i번 사람에게 인사를 하면 L[i]만큼의 체력을 잃고, J[i]만큼의 기쁨을 얻는다. 세준이는 각각의 사람에게 최대 1번만 말할 수 있다.
세준이의 목표는 주어진 체력내에서 최대한의 기쁨을 느끼는 것이다. 세준이의 체력은 100이고, 기쁨은 0이다. 만약 세준이의 체력이 0이나 음수가 되면, 죽어서 아무런 기쁨을 못 느낀 것이 된다. 
세준이가 얻을 수 있는 최대 기쁨을 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
L = [0] + list(map(int, input().split())) 
J = [0] + list(map(int, input().split())) 

dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        if L[i] <= j: # 잃는 체력보다 기쁨이 더 큰 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - L[i]] + J[i]) # 인사를 하지 않을 때의 체력, 인사를 했을 때의 체력
        else: # 인사를 하지 않는게 나은 경우
            dp[i][j] = dp[i-1][j]

print(dp[N][99])

'''
N = int(input())
L = list(map(int, input().split())) 
J = list(map(int, input().split())) 

def BT(life, joy, n) :
    global res

    if n == N and life < 100 :
        res.append(joy)
        return
    else : 
        for i in range(n, N) :
            BT(L[i]+life, J[i]+joy, i+1) # 인사를 하는 경우
            BT(life, joy, i+1) # 인사를 하지 않고 넘어가는 경우

res = []
BT(0,0,0)
print(max(res))
'''
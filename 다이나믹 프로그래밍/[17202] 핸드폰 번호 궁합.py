'''
[17202] 핸드폰 번호 궁합 / Bronze 1 / 다이나믹 프로그래밍
핸드폰 번호 궁합을 보기 위해서는 먼저 궁합을 보고싶은 두 중앙대생 A와 B의 핸드폰 번호에서 맨 앞의 010과 "-"(하이픈)을 모두 제외한 후, A부터 시작하여 한 숫자씩 번갈아가면서 적는다.
그리고 인접한 두 숫자끼리 더한 값의 일의 자리를 두 숫자의 아래에 적어나가면서 마지막에 남는 숫자 2개로 궁합률을 구하게 된다.
핸드폰 번호 궁합률을 알아보는 프로그램을 작성해보자.
'''
import sys
input = sys.stdin.readline

A = list(map(int, input().rstrip()))
B = list(map(int, input().rstrip()))
dp = []
for i in range(8):
    dp.append(A[i])
    dp.append(B[i])

for i in range(15,1,-1):
    for j in range(i):
        dp[j] = (dp[j] + dp[j+1]) % 10

print(*dp[0:2], sep='')
'''
[11399] ATM / Silver 4 / 그리디 알고리즘, 정렬
줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.
'''
N = int(input())
P = list(map(int, input().split()))

P.sort() # 인출하는데 걸리는 시간이 적은 사람을 앞에 배치

for i in range(1, N) :
    P[i] += P[i-1]

print(sum(P))
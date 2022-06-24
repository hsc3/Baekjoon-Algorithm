'''
[10973] 이전 순열 / Silver 3 / 조합론
1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 바로 이전에 오는 순열을 구하는 프로그램을 작성하시오.
사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.
'''
import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

for i in range(N-1, 0, -1) :
    if num[i-1] > num[i] :
        for j in range(N-1, 0, -1) :
            if num[i-1] > num[j] :
                num[i-1], num[j] = num[j], num[i-1]
                num = num[:i] + sorted(num[i:], reverse=True)
                print(*num)
                exit()
print(-1)
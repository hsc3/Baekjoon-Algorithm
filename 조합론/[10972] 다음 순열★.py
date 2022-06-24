'''
[10972] 다음 순열 / Silver 3 / 조합론
1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.
사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.
'''
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))   # s = [1,2,4,3]
x = 0
for i in range(n - 1, 0, -1):         
    if s[i - 1] < s[i]:
        x = i - 1                     # x = 1 (2의 인덱스)
        break
for i in range(n - 1, 0, -1):
    if s[x] < s[i]:                  #  i = 3 (3의 인덱스)
        s[x], s[i] = s[i], s[x]      #  s = [1,3,4,2] 
        s = s[:x + 1] + sorted(s[x + 1:])  # s = [1,3,2,4]
        print(*s)
        exit()
print(-1)
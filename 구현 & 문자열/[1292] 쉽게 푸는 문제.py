# [1292] 쉽게 푸는 문제
# Silver 5 >> 수학, 구현

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
idx = 1
num = 1
res = 0
cnt = 0

while True :
    if cnt == num :
        cnt = 0
        num += 1

    if idx == b + 1 : 
        break
    elif a <= idx <= b :
        res += num

    cnt += 1
    idx += 1

print(res)

'''
A, B = map(int, input().split())
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
print(sum(arr[A:B+1]))
'''
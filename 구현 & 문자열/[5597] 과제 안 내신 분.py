# [5597] 과제 안 내신 분..?
# Bronze 2 >> 구현

import sys 
input = sys.stdin.readline
'''
check = [False] * 30
res = []

for _ in range(28) :
    check[int(input())-1] = True

for i in range(30) :
    if check[i] == False :
        res.append(i+1)

print(*res, sep='\n')
'''

check = [i for i in range(1, 31)]
for _ in range(28) :
    check.remove(int(input()))
print(*check, sep = '\n')
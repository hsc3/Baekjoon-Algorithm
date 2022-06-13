# [2577] 숫자의 개수
# Bronze 2 >> 구현, 수학

numCheck = [0] * 10 # 0 ~ 9

A = int(input())
B = int(input())
C = int(input())

for num in str(A*B*C):
    numCheck[int(num)] += 1 

print(*numCheck, sep='\n')
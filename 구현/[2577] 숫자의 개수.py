# [2577] 숫자의 개수 / Bronze 2 / 구현
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

numCheck = [0] * 10 # 0 ~ 9

A = int(input())
B = int(input())
C = int(input())

for num in str(A*B*C):
    numCheck[int(num)] += 1 

print(*numCheck, sep='\n')
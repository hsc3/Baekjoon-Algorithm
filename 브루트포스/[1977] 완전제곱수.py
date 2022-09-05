# [1977] 완전제곱수 | Bronze 2 | 브루트포스
'''
M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.
'''
from math import sqrt

N = int(input())
M = int(input())

answer = []
for num in range(N, M+1):
    if sqrt(num) % 1 == 0:
        answer.append(num)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))

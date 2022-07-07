'''
[2693] N번째 큰 수 / Silver 5 / 정렬
배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.
배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.
'''
import sys
input = sys.stdin.readline

res = []
for _ in range(int(input())) :
    res.append(sorted(list(map(int, input().split())), reverse = True)[2])

print(*res, sep = '\n')
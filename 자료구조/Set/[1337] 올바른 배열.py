'''
[1337] 올바른 배열 / Silver 4 / 자료구조(Set)
올바른 배열이란 어떤 배열 속에 있는 원소 중 5개가 연속적인 것을 말한다. (연속적인 것이란 5개의 수를 정렬했을 때, 인접한 수의 차이가 1인 것을 말한다.)
배열이 주어지면, 이 배열이 올바른 배열이 되게 하기 위해서 추가되어야 할 원소의 개수를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

arr = set()
for _ in range(int(input())) :
    arr.add(int(input()))

res = 5
for number in arr :
    rightArr = set(number+i for i in range(5)) # number로 시작하는 올바른 배열
    need = len(rightArr-arr)
    res = min(need, res)

print(res)

    
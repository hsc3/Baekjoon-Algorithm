'''
[4158] CD / Silver 5 / 자료구조(Set)
상근이와 선영이는 동시에 가지고 있는 CD를 팔려고 한다. CD를 몇 개나 팔 수 있을까?
'''
import sys
input = sys.stdin.readline

while True :
    N, M = map(int, input().split())
    if N == 0 and M == 0 :
        break

    sanggeun = set()
    sunyoung = set()

    for _ in range(N) :
        sanggeun.add(int(input()))

    for _ in range(M) :
        sunyoung.add(int(input()))

    print(len(sanggeun.intersection(sunyoung)))

'''
import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    s = set(int(input()) for _ in range(N))
    print(sum(1 for _ in range(M) if int(input()) in s))
'''
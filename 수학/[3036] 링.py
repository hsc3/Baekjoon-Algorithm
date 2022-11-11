# [3036] 링 | Silver 4 | https://www.acmicpc.net/problem/3036
import sys
input = sys.stdin.readline

def findGcd(r1, r2):
    if r2 == 0:
        return r1
    return findGcd(r2, r1 % r2)


if __name__ == "__main__":
    answer = []

    N = int(input())
    rings = list(map(int, input().split()))

    for i in range(1, N):
        gcd = findGcd(rings[0], rings[i])
        answer.append("{}/{}".format(rings[0] // gcd, rings[i] // gcd))

    print(*answer, sep='\n')
# [5618] 공약수 | Bronze 2 | 브루트포스
'''
자연수 n개가 주어진다. 이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def GCD(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        return GCD(n2, n1 % n2)

if __name__ == "__main__":
    n = int(input())
    number = sorted(list(map(int, input().split())), reverse=True)

    # 최대공약수 탐색
    if n == 2:
        gcd = GCD(number[0], number[1])
    else: # n == 3
        gcd = GCD(GCD(number[0], number[1]), number[2])

    # 최대공약수의 약수 탐색
    answer = set()
    for i in range(1, int(gcd**(1/2))+1): # 1에서 최대공약수의 제곱근까지 탐색 (ex) 1 ~ 5
        if gcd % i == 0:
            answer.add(i)         # 1, 5
            answer.add(gcd // i)  # 25, 5

    print(*sorted(list(answer)), sep='\n') # 1, 5, 25
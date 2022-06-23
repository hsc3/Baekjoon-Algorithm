'''
[1822] 차집합 / Silver 4 / 자료구조(Set)
몇 개의 자연수로 이루어진 두 집합 A와 B가 있다. 집합 A에는 속하면서 집합 B에는 속하지 않는 모든 원소를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

res = sorted(A-B) # B에 속하지 않는 A의 원소 추출

print(len(res))
if res :
    print(*res)

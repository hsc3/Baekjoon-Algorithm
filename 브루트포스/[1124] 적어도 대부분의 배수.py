# [1124] 적어도 대부분의 배수 / Bronze 1 / 브루트포스 알고리즘
'''
다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다.
서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.
'''
import itertools, math
print(min([math.lcm(n1, n2, n3) for n1, n2, n3 in itertools.combinations(list(map(int, input().split())), 3)]))
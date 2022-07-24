# [10448] 유레카 이론 / Bronze 1 / 브루트포스
'''
삼각수 Tn(n ≥ 1)는 [그림]에서와 같이 기하학적으로 일정한 모양의 규칙을 갖는 점들의 모음으로 표현될 수 있다. 자연수 n에 대해 n ≥ 1의 삼각수 Tn는 명백한 공식이 있다.
Tn = 1 + 2 + 3 + ... + n = n(n+1)/2
1796년, 가우스는 모든 자연수가 최대 3개의 삼각수의 합으로 표현될 수 있다고 증명하였다. 예를 들어,
4 = T1 + T2
5 = T1 + T1 + T2
6 = T2 + T2 or 6 = T3
10 = T1 + T2 + T3 or 10 = T4
이 결과는 증명을 기념하기 위해 그의 다이어리에 “Eureka! num = Δ + Δ + Δ” 라고 적은것에서 유레카 이론으로 알려졌다. 꿍은 몇몇 자연수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 궁금해졌다.
위의 예시에서, 5와 10은 정확히 3개의 삼각수의 합으로 표현될 수 있지만 4와 6은 그렇지 않다.
자연수가 주어졌을 때, 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 없는지를 판단해주는 프로그램을 만들어라. 단, 3개의 삼각수가 모두 달라야 할 필요는 없다.
'''

triangle = [n*(n+1)//2 for n in range(1, 46)] # 삼각수를 계산한 배열 생성
eureka = [0] * 1001

for i in triangle:
    for j in triangle:
        for k in triangle:
            if i+j+k <= 1000:
                eureka[i+j+k] = 1 # 삼각수의 합으로 표현 O

T = int(input())
for _ in range(T):
    print(eureka[int(input())])

'''
import itertools

T = int(input())
N = [int(input()) for _ in range(T)]
maximum_number = max(N)
n = 1
t = []
while int(n * (n + 1) / 2) < maximum_number :
    t.append(int(n * (n + 1) / 2))
    n += 1
t = [sum(x) for x in itertools.product(t, t, t)]
for num in N :
    if t.count(num) >= 1 : print(1)
    else : print(0)
'''
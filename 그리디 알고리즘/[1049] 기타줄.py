# [1049] 기타줄 / Silver 4 / 그리디 알고리즘
'''
Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다. 따라서 새로운 줄을 사거나 교체해야 한다.
강토는 되도록이면 돈을 적게 쓰려고 한다. 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때,
적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
brand = []
for _ in range(M) :
    brand.append(list(map(int, input().split())))

package = float("inf")
each = float("inf")
for i in range(M) :
    # greedy : 패키지 단위로 우선 구매
    package = min(package, brand[i][0], brand[i][1]*6)
    each = min(each, brand[i][0], brand[i][1]*(N%6))

print(package*(N//6) + each)
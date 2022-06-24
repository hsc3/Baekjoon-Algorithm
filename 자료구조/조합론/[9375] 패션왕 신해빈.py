'''
[9375] 패션왕 신해빈 / Silver 3 / 조합론, 자료구조(Dictionary)
해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다.
예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경 대신 렌즈를 착용하거나 해야한다.
해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
'''
import sys
input = sys.stdin.readline
from itertools import product

res = []

for _ in range(int(input())) :
    clothes = dict()
    for _ in range(int(input())) :
        name, species = input().split() # 옷의 이름, 종류
        clothes[species] = clothes.get(species, 0) + 1 # 옷의 종류에 해당하는 값(해당 종류의 옷의 수) + 1

    style = 1
    for species in clothes.keys() :
        style *= (clothes[species] + 1) # 입을 수 있는 모든 스타일 조합 (입지 않는 경우까지)
    res.append(style - 1) # 아무 것도 입지 않은 경우를 제외한 모든 패션 스타일 수

print(*res, sep='\n')

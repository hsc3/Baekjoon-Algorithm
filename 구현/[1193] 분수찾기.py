# [1193] 분수찾기 / Bronze 1 / 구현
'''
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
'''
N = int(input())

num = 1
addNum = 1
while True :
    if num > N : 
        break

    num += addNum
    addNum += 1

bunmo = num-N
bunja = addNum-(num-N)

if addNum % 2 != 0 :
    bunmo, bunja = bunja, bunmo

print("{}/{}".format(bunmo, bunja))
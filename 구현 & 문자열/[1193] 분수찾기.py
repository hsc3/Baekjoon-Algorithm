# [1193] 분수찾기
# Bronze 1 >> 수학, 구현

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
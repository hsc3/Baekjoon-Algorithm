'''
[1076] 저항 / Bronze 2 / 구현
입력으로 주어진 저항의 저항값을 계산하는 프로그램을 작성하시오.
저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다. 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다.
'''


import sys
input = sys.stdin.readline
colorDict = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4, 'green' : 5,
             'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}

inputColor = [input().rstrip() for _ in range(3)]

number = ''
res = 0
for i in range(3) :
    if i != 2 :
        number += str(colorDict[inputColor[i]])
    else :
        res = 10 ** (colorDict[inputColor[i]]) * int(number)

print(res)
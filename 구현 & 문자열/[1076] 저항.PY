# [1076] 저항
# Bronze 2 >> 구현, 딕셔너리

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
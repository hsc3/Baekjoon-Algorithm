'''
[9465] 스티커 / Silver 1 / 다이나믹 프로그래밍
스티커는 2행 n열로 배치되어 있다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다.
모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

for _ in range(int(input())) : # test case
    n = int(input())
    sticker = []
    for _ in range(2) :
        sticker.append(list(map(int, input().split())))
    
    for i in range(1, n) :
        if i == 1 :
            sticker[0][i] += sticker[1][i-1]
            sticker[1][i] += sticker[0][i-1]
        else :
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])
    print(max(sticker[0][n-1], sticker[1][n-1]))

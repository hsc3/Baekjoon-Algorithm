'''
[2002] 추월 / Silver 1 / 구현, 자료구조(Queue)
소문난 명콤비 경찰 대근이와 영식이가 추월하는 차량을 잡기 위해 한 터널에 투입되었다. 대근이는 터널의 입구에, 영식이는 터널의 출구에 각각 잠복하고,
대근이는 차가 터널에 들어가는 순서대로, 영식이는 차가 터널에서 나오는 순서대로 각각 차량 번호를 적어 두었다.
N개의 차량이 지나간 후, 대근이와 영식이는 자신들이 적어 둔 차량 번호의 목록을 보고, 터널 내부에서 반드시 추월을 했을 것으로 여겨지는 차들이 몇 대 있다는 것을 알게 되었다.
대근이와 영식이를 도와 이를 구하는 프로그램을 작성해 보자.
'''
import sys
input = sys.stdin.readline

N = int(input())
tunnelIn = [input().rstrip() for _ in range(N)]
tunnelOut = [input().rstrip() for _ in range(N)]

res = 0
overtaking = False # 추월했는지 여부를 체크

while tunnelIn :
    idx = 0
    outCar = tunnelOut.pop(0) # 터널을 빠져나오는 차량
    if tunnelIn[idx] == outCar : # 추월하지 않은 차에 해당하는 경우
        tunnelIn.pop(0)
    else : # 추월한 차에 해당하는 경우
        overtaking = True
        idx += 1
        res += 1

    while overtaking : # 추월을 한 것으로 판단된 경우, 추월한 차량을 찾는다
        if tunnelIn[idx] == outCar :
            tunnelIn.pop(idx)
            overtaking = False
        else :
            idx += 1

print(res)

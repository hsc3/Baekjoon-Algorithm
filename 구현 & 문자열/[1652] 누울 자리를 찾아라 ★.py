'''
Bronze 1 [1652] 누울 자리를 찾아라 | 구현, 문자열
코레스코 콘도에 있는 방은 NxN의 정사각형 모양으로 생겼다. 방 안에는 옮길 수 없는 짐들이 있어서 누울 자리를 차지하고 있었다.
영식이가 누울 수 있는 자리에는 조건이 있다. 
- 똑바로 연속해서 <<2칸 이상>>의 빈 칸이 존재하면 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있다. 
- 가로로 누울 수도 있고 세로로 누울 수도 있다. 
첫째 줄에 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 개수를 출력하는 프로그램을 작성하라.
'''
# zip을 활용하여 배열의 x, y축을 손쉽게 변경할 수 있다. 
import sys
input = sys.stdin.readline

def Checkspace(r) :
    res = 0
    for i in range(n) :
        chk = 0
        for j in range(n) :
            if r[i][j] == '.' :
                chk += 1
            elif r[i][j] == 'X' :
                if chk >= 2 :
                    res += 1
                chk = 0
        if chk >= 2 : # 벽의 끝에 닿았을 경우.
            res += 1
    return res

room = []
n = int(input())
for _ in range(n) : # 방의 구조 입력
    room.append(input().rstrip())

print(Checkspace(room), Checkspace(list(zip(*room))))
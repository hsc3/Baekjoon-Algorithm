'''
[2711] 오타맨 고창영 / Bronze 2 / 문자열
고창영은 맨날 오타를 낸다. 창영이가 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 오타를 지운 문자열을 출력하는 프로그램을 작성하시오.
창영이는 오타를 반드시 1개만 낸다.
'''
import sys
input = sys.stdin.readline

res = []

for _ in range(int(input())) :
    inputData = list(input().split())
    inputData[1] = inputData[1][:int(inputData[0])-1] + inputData[1][int(inputData[0]):]
    res.append(inputData[1])

    #idx, string = int(inputData[0])-1, list(inputData[1].rstrip())
    #string.pop(idx)
    #res.append(''.join(string))

print(*res, sep = '\n')

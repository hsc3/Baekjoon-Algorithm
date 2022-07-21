'''
[17608] 막대기 / Bronze 2 / 구현
높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, N개의 막대기에 대한 
높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하자.
'''
import sys
input = sys.stdin.readline

res = 0
stick = [int(input()) for _ in range(int(input()))]

max_height = 0
for height in stick[::-1] :
    if height > max_height :
        res += 1
        max_height = height

print(res)
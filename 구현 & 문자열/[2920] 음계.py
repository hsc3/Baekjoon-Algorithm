# [2920] 음계 | Bronze 2 | 구현
import sys
input = sys.stdin.readline

data = list(map(int, input().split()))

if data == sorted(data) :
    print("ascending")
elif data == sorted(data, reverse = True) :
    print("descending")
else :
    print("mixed")
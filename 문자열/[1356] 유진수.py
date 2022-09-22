# [1356] 유진수 | Bronze 1 | https://www.acmicpc.net/problem/1356
import sys
input = sys.stdin.readline

number = list(map(int, input().rstrip()))

idx = 1 # 왼쪽과 오른쪽을 구분하는 인덱스
check = False
while idx < len(number):
    left = 1 # 왼쪽에서의 곱셈 결과
    for i in range(0, idx):
        left *= number[i]

    right = 1 # 오른쪽에서의 곱셈 결과
    for i in range(idx, len(number)):
        right *= number[i]

    if left == right:
        check = True
        break
    idx += 1

print("YES" if check else "NO")


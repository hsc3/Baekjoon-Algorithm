# [3062] 수 뒤집기 | Bronze 2 | https://www.acmicpc.net/problem/3062
import sys
input = sys.stdin.readline

answer = []

T = int(input())
for _ in range(T):
    num = str(input().rstrip())
    data = str(int(num) + int(num[::-1]))
    if data == data[::-1]:
        answer.append("YES")
    else:
        answer.append("NO")

print(*answer, sep='\n')
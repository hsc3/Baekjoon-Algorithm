# [ 9342 ] 염색체 | Silver 3 | https://www.acmicpc.net/problem/9342
import sys
input = sys.stdin.readline

def Checker(str):
    if len(str) == 3:
        if str == "AFC":
            return True
    elif len(str) == 4:
        if str[:3] == "AFC" and str[3] in ['A', 'B', 'C', 'D', 'E', 'F']:
            return True
        if str[1:] == "AFC" and str[0] in ['A', 'B', 'C', 'D', 'E', 'F']:
            return True
    elif len(str) == 5:
        if str[1:4] == "AFC" and str[0] in ['A', 'B', 'C', 'D', 'E', 'F'] and str[-1] in ['A', 'B', 'C', 'D', 'E', 'F']:
            return True
    return False

answer = []
T = int(input())
for _ in range(T):
    str = list(input().rstrip())
    idx = 0
    while idx < len(str)-1: # 연속된 중복 문자 제거
        if str[idx] == str[idx+1]:
            str.pop(idx+1)
        else:
            idx += 1

    answer.append("Infected!" if Checker(''.join(str)) else "Good")

print(*answer, sep='\n')
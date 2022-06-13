# [2908] 상수
# Bronze 2 >> 수학, 구현

import sys
input = sys.stdin.readline

A, B = input().split()
print(A[::-1] if A[::-1] > B[::-1] else B[::-1]) 
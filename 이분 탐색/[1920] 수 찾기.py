# [1920] 수 찾기 | Silver 4 | 이분 탐색
'''
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
'''
import sys
input = sys.stdin.readline

def BS(num, s, e) :
    if s > e : return 0
    m = (s + e) // 2 
    if N[m] == num :  return 1
    elif N[m] > num : return BS(num, s, m-1)
    elif N[m] < num : return BS(num, m+1, e) 

n = int(input())
N = sorted(list(map(int, input().split())))
m = int(input())
M = list(map(int, input().split()))
for num in M : print(BS(num, 0, n-1))
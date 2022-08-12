'''
[9934] 완전 이진 트리 | Silver 1 | 자료구조 (Tree)
상근이가 종이에 적은 순서(중위순회)가 모두 주어졌을 때, 각 레벨에 있는 빌딩의 번호를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
def recur(i, t) :
    if i > K :
        return
    mid = len(t)//2
    level[i].append(t[mid])
    recur(i+1, t[:mid]) # 왼쪽 서브트리 탐색
    recur(i+1, t[mid+1:]) # 오른쪽 서브트리 탐색

K = int(input())
tree = list(map(int, input().split()))
level = [[]for _ in range(K+1)]
recur(1, tree)
for i in range(1, K+1) :
    print(*level[i])
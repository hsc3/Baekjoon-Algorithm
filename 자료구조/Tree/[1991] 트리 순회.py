'''
[1991] 트리 순회 | Silver 1 | 자료구조 (Tree)
이진 트리를 입력받아 전위 순회, 중위 순회, 후위 순회한 결과를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def Preorder(root) : 
    if root != '.' :
        print(root, end='')
        Preorder(tree[root][0])
        Preorder(tree[root][1])

def Inorder(root) :
    if root != '.' :
        Inorder(tree[root][0])
        print(root, end='')
        Inorder(tree[root][1])

def Postorder(root) :
    if root != '.' :
        Postorder(tree[root][0])
        Postorder(tree[root][1])
        print(root, end='')

N = int(input()) # 이진트리의 노드의 개수
tree = {}
for _ in range(N) :
    root, left, right = input().split()
    tree[root] = [left, right]
    # p, l, r = map(lambda x : ord(x) - 65 ,input().split()) 
Preorder('A')
print()
Inorder('A')
print()
Postorder('A')

'''
adj = {}
N = int(input())

for i in range(N):
    A, B, C = input().split()
    if A not in adj:
        adj[A] = [B, C]

# 전위 순회 [root, left, right]
def recur(node, order):
    if node == '.':
        return

    left, right = adj[node]
    if order == 1: # 전위 (DLR)
        print(node, end="")
    recur(left, order)
    if order == 2: # 중위 (LDR)
        print(node, end="")
    recur(right, order)
    if order == 3: # 후위 (LRD)
        print(node, end="")

recur('A', 1)
print()
recur('A', 2)
print()
recur('A', 3)
print()
'''
# [2644] 촌수계산 | Silver 2 | 그래프 (DFS)
'''
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다.
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def DFS(node) :
    stk = [node]
    while stk :
        u = stk.pop()
        for v in adjacent[u] :
            if relation[v] == 0 : # 아직 방문하지 않은 경우, 촌수를 계산합니다.
                relation[v] = relation[u] + 1
                stk.append(v)
   

N = int(input())
x, y = map(int, input().split())
adjacent = [[] for _ in range(101)]
relation = [0] * 101 # 촌수이자 방문여부를 의미

for _ in range(int(input())) :
    s, e = map(int, input().split())
    adjacent[s].append(e)
    adjacent[e].append(s)

# DFS -> stack
DFS(x)
print(relation[y] if relation[y] > 0 else -1)
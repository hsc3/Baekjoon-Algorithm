'''
[1058] 친구 / Silver 3 / 그래프(Floyd-Warshall)
어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 
여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
friend = [list(input().rstrip()) for _ in range(N)]
twoFriend = [[0]*N for _ in range(N)]

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            # i와 j가 직접 친구이거나, k를 건너 친구인 사이이면, i와 j는 2-친구이다.
            if i != j and (friend[i][j] == 'Y' or (friend[i][k] == 'Y' and friend[k][j] == 'Y')) :
                twoFriend[i][j] = 1 

print(max([sum(x) for x in twoFriend]))
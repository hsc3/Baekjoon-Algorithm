'''
[14889] 스타트와 링크 | Silver 2 | 백트랙킹
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.
사람에게 번호를 1부터 N까지로 배정했고, 능력치를 조사했다. i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.
스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.
'''
import sys, itertools
from itertools import permutations, combinations
input = sys.stdin.readline

# N명의 사람을 절반으로 나누고 능력치의 총합을 계산.
def Ability(A, B) :
    global ans

    ability_A = ability_B = 0

    for x, y in permutations(A, 2) :
        ability_A += S[x][y]

    for x, y in permutations(B, 2) :
        ability_B += S[x][y]

    ans = min(ans, abs(ability_A - ability_B))
    return

if __name__ == "__main__":
    N = int(input())
    S = []
    for _ in range(N) :
        S.append(list(map(int, input().split())))

    all = [i for i in range(N)]
    start = list(combinations(all, N//2))
    link = list(reversed(start))

    ans = sys.maxsize
    for i in range(len(start)) :
        Ability(start[i], link[i])

    print(ans)

'''
import sys, itertools
from itertools import permutations, combinations
input = sys.stdin.readline 
# ====================================================================
# N명의 사람을 절반으로 나누고 능력치의 총합을 계산.
def Ability(A, B) :
    global ans
    ability_A = ability_B = 0
    #print("A : {} ,  B : {}".format(team_A, team_B))
    for x, y in permutations(list(A), 2) :
        ability_A += S[x][y]
    for x, y in permutations(list(B), 2) :
        ability_B += S[x][y]
    ans = min(ans, abs(ability_A - ability_B))
    return
# ====================================================================
# 한 팀의 멤버만 고른다. (절반은 Ability 함수에서)
def MakeTeam(team_A, start_idx) :
    if len(team_A) == N / 2 :
        Ability(team_A, allTeam.difference(team_A))
        return
    for idx in range(start_idx, N) :
        if visited[idx] == False :
            team_A.add(idx)
            visited[idx] = True
            MakeTeam(team_A, idx)
            team_A.remove(idx)
            visited[idx] = False
# ====================================================================
N = int(input())
S = []
for _ in range(N) :
    S.append(list(map(int, input().split())))
allTeam = {i for i in range(N)}
visited = [False] * N
ans = float("inf")
team_A = set()
MakeTeam(team_A, 0)
print(ans)
'''
'''
from itertools import combinations
import sys

N = int(input())
power= [list(map(int, input().split())) for _ in range(N)]

numbers = [i for i in range(N)]
start = list(combinations(numbers, N // 2)) # [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
link = list(reversed(start))                # [(2,3), (1,3), (1,2), (0,3), (0,2), (0,1)]

def cal_team_power(team):
    sum = 0
    for i in range(len(team) - 1):
        for j in range(i+1, len(team)):
           sum += power[team[i]][team[j]]
           sum += power[team[j]][team[i]]
    return sum

ans = sys.maxsize
for i in range(len(start) // 2):
    diff = abs(cal_team_power(list(start[i])) - cal_team_power(list(link[i])))
    ans = min(ans, diff)
print(ans)
'''
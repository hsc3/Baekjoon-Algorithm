'''
[1759] 암호 만들기 | Gold 5 | 백트랙킹
암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.
새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다.
C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

# 알파벳 모음(a,e,i,o,u)을 최소 1개는 사용해야 한다.
def IsMoeum(choose) : # 모음 판별 함수
    m = 0
    z = 0

    for i in choose :
        if i in "aeiou" :
            m += 1
        else :
            z += 1
    if m >= 1 and z >= 2 :
        print(choose)

def MakePassword(password) :
    if len(password) == l :
        IsMoeum(password)
        return

    for idx in range(c) :
        if visited[idx] == False and password[len(password)-1] < alphabet[idx] :
            visited[idx] = True
            MakePassword(password+alphabet[idx])
            visited[idx] = False

if __name__ == "__main__":
    l, c = map(int, input().split()) # 암호의 길이, 알파벳의 갯수
    alphabet = sorted(list(input().split())) # 알파벳 리스트
    visited = [False] * c

    for i in range(c) :
        visited[i] = True
        MakePassword(alphabet[i])

'''
import sys
input = sys.stdin.readline

l, c = map(int, input().split()) # 4 6
a = input().split()
default = c - l + 1 # 3

def check(s: str):
    mo = 0
    za = 0
    for i in s:
        if i in "aeoui":
            mo += 1
        else:
            za += 1
        if mo >= 1 and za >= 2:
            return True
    return False

def dfs(cnt: int, p: int, s: str):
    global a
    for i in range(p, default + cnt):
        if cnt == l - 1:
            if check(s + a[i]):
                print(s + a[i])
        else:
            dfs(cnt + 1, i + 1, s + a[i])


a.sort()
for i in range(default):
    dfs(1, i + 1, a[i])
'''

'''
from itertools import combinations as comb

l, c = map(int, input().split())
s = sorted(list(map(str, input().split())))
cb = comb(s, l)

v = ['a', 'e', 'i', 'o', 'u']
t = []
for e in cb:
    i = j = 0
    for k in range(l):
        if e[k] in v: i += 1
        else: j += 1

    if i >= 1 and j >= 2: print(''.join(e))
'''
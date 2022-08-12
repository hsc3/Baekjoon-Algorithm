'''
[17219] 비밀번호 찾기 | Silver 4 | 자료구조 (Map)
Q : 메모장에서 사이트에 해당하는 비밀번호를 찾아주는 프로그램을 만들어보자.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().rsplit())
dic = {}

for _ in range(N) :
    site, password = input().split()
    dic[site] = password # 사이트의 비밀번호 저장

for _ in range(M) :
    question = input().rstrip()
    print(dic[question]) # 사이트의 비밀번호 출력
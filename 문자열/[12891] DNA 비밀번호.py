# [12891] DNA 비밀번호 | Silver 3 | https://www.acmicpc.net/problem/12891
import sys
input = sys.stdin.readline

S, P = map(int, input().split()) # S: DNA 문자열의 길이 , P: 부분문자열의 길이
DNA = input().rstrip()
A, C, G, T = map(int,input().split())

answer = 0
idx = P
dic = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0} # 부분 문자열에 포함된 문자의 갯수
for i in range(idx):
    dic[DNA[i]] += 1

while True:
    if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T: # 모든 문자를 포함한 경우
        answer += 1

    if idx == S:
        break

    dic[DNA[idx]] += 1 # 오른쪽 문자 포함
    dic[DNA[idx-P]] -= 1 # 왼쪽 문자 제거

    idx += 1

print(answer)
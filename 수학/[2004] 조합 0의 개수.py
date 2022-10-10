# [2004] 조합 0의 개수 | Silver 2 | https://www.acmicpc.net/problem/2004

n, m = map(int, input().split())
m = n-m if m > n-m else m

def count(num, d):
    cnt = 0
    while num:
        num //= d
        cnt += num
    return cnt

cnt_two = count(n, 2) - count(n-m, 2) - count(m, 2) # nCm에 포함된 2의 개수
cnt_five = count(n, 5) - count(n-m, 5) - count(m, 5) # nCm에 포함된 5의 개수

print(min(cnt_two, cnt_five))
# [1074] Z | Silver 1 | https://www.acmicpc.net/problem/1074

def recur(r, c, size, num):
    global answer
    if size == 1:
        answer = num
        return

    size //= 2
    if r+size <= R and c+size <= C: # 우측 하단
        recur(r+size, c+size, size, num + ((size)**2)*3)
    elif r+size <= R and c <= C: # 좌측 하단
        recur(r+size, c, size, num + ((size)**2)*2)
    elif r <= R and c+size <= C: # 우측 상단
        recur(r, c+size, size, num + (size)**2)
    else: # 좌측 상단
        recur(r, c, size, num)

N, R, C = map(int, input().split())
answer = 0
recur(0, 0, 2**N, 0)
print(answer)

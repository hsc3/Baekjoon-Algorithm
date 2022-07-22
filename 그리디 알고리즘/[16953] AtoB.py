# [16953] A → B  / Silver 2 / 그리디 알고리즘, 그래프 탐색
'''
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
  2를 곱한다.
  1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
'''
import sys
input = sys.stdin.readline

target, base = map(int, input().strip().split())
answer = 1

while True:
    if base <= target:
        break
    if base % 10 == 1:
        base = base // 10
    elif base % 2 == 0:
        base //= 2
    else:
        break
    answer += 1

print(answer if base == target else '-1')

# A, B = map(int, input().split())
# tmp = [A]
# cnt = 1
# while True :
#     if len(tmp) == 0 : print(-1); exit(0)
#     cnt += 1
#     numList = tmp
#     tmp = []
#     for num in numList :
#         n1 = num*2
#         n2 = num*10+1
#         if n1 == B or n2 == B :
#             print(cnt); exit(0)
#         if n1 < B :
#             tmp.append(n1)
#         if n2 < B :
#             tmp.append(n2)

'''
def BFS() :
    if len(q) == 0 :
        return -1
    tmp = q.popleft()
    n1 = [tmp[0]*2, tmp[1]+1]
    n2 = [tmp[0]*10+1, tmp[1]+1]
    if n1[0] == B or n2[0] == B :
        return n1[1]
    else :
        if n1[0] < B :
            q.append(n1)
        if n2[0] < B :
            q.append(n2)
    return BFS()

A, B = map(int, input().split())
q = deque([[A,1]])
print(BFS())
'''
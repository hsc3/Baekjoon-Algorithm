# [2605] 줄 세우기 | Bronze 2 | 자료구조(queue)
'''
줄을 선 학생들이 차례로 뽑은 번호가 주어질 때 학생들이 최종적으로 줄을 선 순서를 출력하는 프로그램을 작성하시오.
뽑은 번호만큼 앞으로 가서 줄을 서게 된다. 각자 뽑은 번호는 자신이 처음에 선 순서보다는 작은 수이다.
'''
# 선형적인 순서 -> Queue
import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
queue = []

cnt = 0
for i in range(N) :
    queue.insert(cnt - num[i], i+1)
    cnt += 1

print(*queue, sep = ' ')
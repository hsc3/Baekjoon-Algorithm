# [2548] 대표 자연수 | Silver 3 | 정렬
'''
정보초등학교의 연아는 여러 개의 자연수가 주어졌을 때, 이를 대표할 수 있는 대표 자연수에 대하여 연구하였다. 그 결과 어떤 자연수가 다음과 같은 성질을 가지면 대표 자연수로 적당할 것이라고 판단하였다.
“대표 자연수는 주어진 모든 자연수들에 대하여 그 차이를 계산하여 그 차이들 전체의 합을 최소로 하는 자연수이다.”
연아를 도와서 위의 성질을 만족하는 대표 자연수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
number = sorted(list((map(int, input().split())))) # 오름차순 정렬
'''
   |  2    3    4    9   10
----------------------------
2  |  0    1    2    7    8    (18)
3  |  1    0    1    6    7    (15)
4  |  2    1    0    5    6    (14)
9  |  7    6    5    0    1    (19)
10 |  8    7    6    1    0    (22)
'''
minimum = float("inf")
answer = []

for i in range(N//2-1, N): # 정렬된 숫자의 N//2 - 1번째 숫자부터 탐색
    sum_temp = 0 # 차이 합
    for j in range(N):
        sum_temp += abs(number[i] - number[j])
    if minimum < sum_temp: # 이전 최소 값보다 크면 종료
        break
    else:
        minimum = sum_temp
        answer.append([number[i], minimum]) # [숫자, 차이 합] 저장

print(sorted(answer, key=lambda x: (x[1], x[0]))[0][0])

# N = int(input())
# number = sorted(list(map(int, input().split())))
# print(number[N//2-1] if N % 2 == 0 else number[N//2])
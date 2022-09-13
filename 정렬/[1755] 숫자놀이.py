# [1755] 숫자놀이 | Silver 4 | 정렬
'''
79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 80은 마찬가지로 "eight zero"라고 읽는다. 79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.
문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.
'''
en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
M, N = map(int, input().split())
data = []

for number in range(M, N+1):
    english = ' '.join(en[int(n)] for n in str(number)) # 숫자 -> 영어
    data.append([english, number]) # [영어, 숫자]를 저장

data.sort() # 영어 기준으로 정렬

for i in range(len(data)):
    if i != 0 and i % 10 == 0:
        print()
    print(data[i][1], end=' ')
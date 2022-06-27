'''
[2108] 통계학 / Silver 3 / 구현, 정렬
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
- 산술평균 : N개의 수들의 합을 N으로 나눈 값
- 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
- 최빈값 : N개의 수들 중 가장 많이 나타나는 값
- 범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
from collections import Counter

res = []
numbers = list(int(input()) for _ in range(int(input())))

# 1. 산술평균
res.append(round(sum(numbers) / len(numbers)))

# 2. 중앙값
numbers.sort()
res.append(numbers[len(numbers)//2])

# 3. 최빈값
numberCount = Counter(numbers)

if len(numberCount) > 1 and numberCount.most_common(2)[0][1] == numberCount.most_common(2)[1][1] :
    res.append(numberCount.most_common(2)[1][0])
else :
    res.append(numberCount.most_common(1)[0][0])

# 4. 범위
res.append(numbers[-1] - numbers[0])

print(*res, sep = '\n')
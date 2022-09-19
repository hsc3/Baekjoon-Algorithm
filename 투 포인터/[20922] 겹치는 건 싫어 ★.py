# [20922] 겹치는 건 싫어 | Silver 1 | 투 포인터
'''
홍대병에 걸린 도현이는 겹치는 것을 매우 싫어한다. 특히 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어한다. 도현이를 위해 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구하려고 한다.
100,000 이하의 양의 정수로 이루어진 길이가 N인 수열이 주어진다. 이 수열에서 같은 정수를 K개 이하로 포함한 최장 연속 부분 수열의 길이를 구하는 프로그램을 작성해보자.
'''
import sys
input = sys.stdin.readline
from collections import defaultdict

N, K = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 1
counter = defaultdict(int)
counter[arr[0]] = 1
answer = 1
maxLength = 1

while right < N:
    # 일단 오른쪽(arr[right]) 숫자를 포함시킨다.
    counter[arr[right]] += 1
    maxLength += 1
    # 해당 숫자가 K개를 초과하게 될 경우 -> 초과하지 않을 때까지 왼쪽 숫자(arr[left])를 제거한다.
    if counter[arr[right]] > K:
        while counter[arr[right]] > K:
            counter[arr[left]] -= 1
            left += 1
            maxLength -= 1

    right += 1
    if answer < maxLength:
        answer = maxLength

print(answer)
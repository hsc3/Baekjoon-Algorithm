# [16401] 과자 나눠주기 | Silver 2 | 이분 탐색
'''
명절이 되면, 홍익이 집에는 조카들이 놀러 온다. 떼를 쓰는 조카들을 달래기 위해 홍익이는 막대 과자를 하나씩 나눠준다.
조카들이 과자를 먹는 동안은 떼를 쓰지 않기 때문에, 홍익이는 조카들에게 최대한 긴 과자를 나눠주려고 한다.
그런데 나눠준 과자의 길이가 하나라도 다르면 조카끼리 싸움이 일어난다. 따라서 반드시 모든 조카에게 같은 길이의 막대 과자를 나눠주어야 한다.
M명의 조카가 있고 N개의 과자가 있을 때, 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 구하라.
단, 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만, 과자를 하나로 합칠 수는 없다. 단, 막대 과자의 길이는 양의 정수여야 한다.
'''
import sys
input = sys.stdin.readline

def GiveSnack(snackLength): # SnackLength 길이 만큼 조카에게 모두 과자를 나눠줄 수 있는지 판별
    cnt = 0
    for s in snack:
        cnt += (s // snackLength) # 막대 과자를 가능한 snackLength 길이 여러 개로 쪼갠다.

    return True if cnt >= M else False

if __name__ == "__main__":
    M, N = map(int, input().split())
    snack = list(map(int, input().split()))

    answer = 0 # 막대 과자의 최대 길이
    left, right = 1, max(snack)

    while left <= right: # 막대 과자의 길이를 기준으로 이분 탐색을 수행한다.
        mid = (left + right) // 2

        if GiveSnack(mid): # 해당 길이의 막대 과자를 조카에게 모두 나눠줄 수 있는 경우
            left = mid + 1 # 막대 과자의 길이를 늘린다.
            answer = max(answer, mid) # 막대 과자의 최대 길이를 저장한다.

        else: # 해당 길이의 막대 과자를 조카에게 모두 나눠줄 수 없는 경우
            right = mid - 1 # 막대 과자의 길이를 줄인다.

print(answer)
# [2343] 기타 레슨 | Silver 1 | 이분 탐색
'''
강토는 자신의 기타 강의 동영상을 블루레이로 만들어 판매하려고 한다. 블루레이에는 총 N개의 강의가 들어가는데, 블루레이를 녹화할 때, 강의의 순서가 바뀌면 안 된다.
순서가 뒤바뀌는 경우에는 강의의 흐름이 끊겨, 학생들이 대혼란에 빠질 수 있기 때문이다. 즉, i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화해야 한다.

강토는 이 블루레이가 얼마나 팔릴지 아직 알 수 없기 때문에, 블루레이의 개수를 가급적 줄이려고 한다. 오랜 고민 끝에 강토는 M개의 블루레이에 모든 기타 강의 동영상을 녹화하기로 했다.
이때, 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 같은 크기이어야 한다.

강토의 각 강의의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.
'''
# <<이분탐색의 대상>>은 블루레이의 크기이다!!

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 강의의 수, 블루레이의 수
video = list(map(int, input().split()))

left, right = max(video), sum(video) # 이분탐색으로 탐색할 블루레이 크기
answer = sum(video)

while left <= right:
    mid = (left + right) // 2 # mid = 블루레이의 적정 크기
    blueray_cnt = 1 # mid 만큼 동영상을 담을 때, 만들어지는 블루레이 갯수
    blueray_length = 0 # 만들어지고 있는 블루레이의 동영상 길이
    # print("left: {}, mid: {}, right: {}".format(left, mid, right))

    # [1] 블루레이에 동영삼을 담는다.
    for i in range(N):
        if blueray_length + video[i] <= mid: # 아직 블루레이에 동영상을 더 담을 수 있는 경우
            blueray_length += video[i]
            # print("{}를 블루레이 {}에 담습니다. 블루레이{}의 길이는 {}입니다.".format(video[i], blueray_cnt, blueray_cnt, blueray_length))

        else: # 블루레이에 동영상을 더 담을 수 없는 경우
            blueray_cnt += 1
            blueray_length = video[i]
            # print("블루레이 {}가 가득 차버리므로, {}를 블루레이 {}에 담습니다. 블루레이 {}의 길이는 {}입니다.".format(blueray_cnt-1, video[i], blueray_cnt, blueray_cnt, blueray_length))


    # [2] 만들어진 블루레이의 갯수를 확인한다.
    if blueray_cnt > M: # 사용할 수 있는 블루레이 갯수를 넘은 경우 -> 블루레이의 크기를 키운다.
        # print("-> 사용된 블루레이가 {}개로 {}개보다 많습니다. 블루레이의 크기를 키웁니다.".format(blueray_cnt, M))
        left = mid + 1

    elif blueray_cnt <= M: # 사용할 수 있는 블루레이 갯수가 남거니 딱 M개만큼 사용한 경우 -> 블루레이의 크기를 줄여본다.
        # print("-> 사용된 블루레이가 {}개로 {}개보다 적거나 같습니다. 블루레이의 크기를 더 줄여봅니다.".format(blueray_cnt, M))
        answer = min(answer, mid)
        right = mid - 1

print(answer)
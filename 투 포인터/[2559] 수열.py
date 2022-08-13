# [2559] 수열 | Silver 3 | 투 포인터
'''
매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.
입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 날짜의 수 , 합을 구하기 위한 연속적인 날짜의 수
temperature = list(map(int, input().split()))

start = 0
end = K
tmp = sum(temperature[start:end])
answer = [tmp]
while start < N-K:
    # 슬라이딩 윈도우를 오른쪽으로 1칸씩 이동하면서 온도의 합 저장
    tmp -= temperature[start]
    tmp += temperature[end]
    answer.append(tmp)
    start += 1
    end += 1

print(max(answer))
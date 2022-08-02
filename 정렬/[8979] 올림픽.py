# [8979] 올림픽 | Silver 5 | 정렬
'''
올림픽은 참가에 의의가 있기에 공식적으로는 국가간 순위를 정하지 않는다. 그러나, 많은 사람들이 자신의 국가가 얼마나 잘 하는지에 관심이 많기 때문에 비공식적으로는 국가간 순위를 정하고 있다.
두 나라가 각각 얻은 금, 은, 동메달 수가 주어지면, 보통 다음 규칙을 따라 어느 나라가 더 잘했는지 결정한다.
- 금메달 수가 더 많은 나라
- 금메달 수가 같으면, 은메달 수가 더 많은 나라
- 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라
각 국가는 1부터 N 사이의 정수로 표현된다. 한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의된다. 만약 두 나라가 금, 은, 동메달 수가 모두 같다면 두 나라의 등수는 같다.
각 국가의 금, 은, 동메달 정보를 입력받아서, 어느 국가가 몇 등을 했는지 알려주는 프로그램을 작성하시오.
'''
def CheckRanking(data, K) :
    rank = 1
    count = 1
    for i in range(len(data)) :
        if data[i][0] == K :
            return rank
        else :
            if data[i][1:] != data[i + 1][1:] : 
                rank += count
                count = 1
            else : # 공동
                count += 1

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
data = []
for _ in range(N) :
    num, gold, silver, bronze = map(int, input().split())
    data.append([num, gold, silver, bronze])
data.sort(key = lambda x : (-x[1], -x[2], -x[3]))
print(CheckRanking(data, K))

'''
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(n)]
score.sort(key = lambda x : (x[1], x[2], x[3]), reverse = True)

for i in range(n):
    if score[i][0] == k:
        target = i
        break

for idx,nation in enumerate(score, 1):
    if score[target][1:] == nation[1:]:
        print(idx)
        break
'''
'''
[5800] 성적 통계 / Silver 5 / 정렬
한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다. 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.
중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

첫째 줄에는 "Class X"를 출력한다. X는 반의 번호이며 입력으로 주어진 순서대로 1부터 증가한다.
둘째 줄에는 가장 높은 점수, 낮은 점수, 성적을 내림차순으로 정렬했을 때 가장 큰 인접한 점수 차이를 예제 출력과 같은 형식으로 출력한다.
'''
import sys
input = sys.stdin.readline

answer = []
for i in range(int(input())):
    grades = sorted(list(map(int, input().split()))[1:], reverse=True) # 내림차순 정렬
    largestGap = max([grades[i] - grades[i+1] for i in range(len(grades)-1)])
    answer.append([grades[0], grades[-1], largestGap])

for i in range(len(answer)) :
    print("Class {}".format(i+1))
    print("Max {}, Min {}, Largest gap {}".format(*answer[i]))
    
# [10825] 국영수 | Silver 4 | 정렬
'''
Q: 도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 
이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
----------------------------------------------------------------------------------------------------------------
- 국어 점수가 감소하는 순서로
- 국어 점수가 같으면 영어 점수가 증가하는 순서로
- 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
- 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
'''

N = int(input())
data = []
for _ in range(N) :
    name, k, e, m = input().split()
    student = {} # 딕셔너리 
    student['name'] = name
    student['korean'] = int(k)
    student['english'] = int(e)
    student['math'] = int(m)
    data.append(student)
data.sort(key = lambda x : (-x['korean'], x['english'], -x['math'], x['name'])) # 다중조건 ★
for student in data :
    print(student['name'])


'''
from functools import cmp_to_key
# return 1, 0, -1
def mySort(student1, student2) :
    if student1[1] < student2[1] : # 국어점수가 감소하는 순서
        return 1
    elif student1[1] > student2[1] : 
        return -1 
    else : # 국어점수가 같은 경우
        if student1[2] > student2[2] : # 영어점수가 증가하는 순서
            return 1
        elif student1[2] < student2[2] :
            return -1
        else : # 국어, 영어점수가 같은 경우
            if student1[3] < student2[3] : # 수학점수가 감소하는 순서
                return 1
            elif student1[3] > student2[3] : 
                return -1 
            else : # 국어, 영어, 수학점수가 같은 경우
                if student1[0] > student2[0] : # 이름이 사전순으로 증가하는 순서
                    return 1
                else : 
                    return -1
'''
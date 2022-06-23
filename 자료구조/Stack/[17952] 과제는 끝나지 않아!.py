'''
[17952] 과제는 끝나지 않아! / Silver 3 / 자료구조(스택)
아래와 같은 규칙으로 과제를 해 나가고 있다.
1. 과제는 가장 최근에 나온 순서대로 한다. 또한 과제를 받으면 바로 시작한다.
2. 과제를 하던 도중 새로운 과제가 나온다면, 하던 과제를 중단하고 새로운 과제를 진행한다.
3. 새로운 과제가 끝났다면, 이전에 하던 과제를 이전에 하던 부분부터 이어서 한다.
성애는 과제를 받자마자 이 과제가 몇 분이 걸릴지 정확하게 알 수 있고, 성애가 제출한 과제는 무조건 만점을 받는다.
성애가 받을 과제 점수를 구해주는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input()) # 이번 학기의 시간(분)
homeworkList = [] # 성애가 해야 할 과제 리스트
res = 0 # 성애가 받을 과제 점수

for i in range(N) :
    inputList = list(map(int, input().split()))
   
    if inputList[0] == 1 : # 과제가 주어진 경우
        homeworkList.append(inputList[1:]) # 일단 과제 리스트에 넣는다.
    
    if homeworkList : # 수행할 과제가 있는 경우
        homework = homeworkList.pop() # 지금 진행할 과제(가장 최근에 받은 과제)를 리스트에서 pop
        homework[1] -= 1 # 과제 수행 (과제 시간 -= 1)
              
        if homework[1] == 0 : # 과제를 모두 수행한 경우, 과제 점수를 합산한다.
            res += homework[0]
        else :
            homeworkList.append(homework) # 과제를 모두 수행하지 못한 경우, 다시 리스트의 뒤에 push
        
print(res)

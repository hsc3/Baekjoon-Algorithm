'''
[1966] 프린터 큐 / Silver 3 / 구현, 시뮬레이션, 자료구조(큐)
프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.
- 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
- 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.
'''
import sys 
input = sys.stdin.readline

res = []

for _ in range(int(input())) :
    
    N, M = map(int, input().split()) # N : 문서의 개수, M : 알고자 하는 문서의 현재 인덱스
    printer = [t for t in enumerate(list(map(int, input().split())))] # (문서의 인덱스, 중요도) 형태로 저장
    importance = [x[1] for x in printer] # 문서의 중요도만 따로 저장
    
    cnt = 1 # 인쇄 순서
    while True :
        document = printer.pop(0) # 다음으로 인쇄하고자 하는 문서
        
        if document[1] == max(importance) : # 다음으로 인쇄할 문서가 가장 중요도가 높은 경우    
            if document[0] == M : # 알고자 하는 어떤 한 문서인 경우
                break
        
            importance.remove(document[1]) # 인쇄한 문서의 중요도는 삭제
            cnt += 1 # 인쇄 순서 1 증가
        
        else : # 다음으로 인쇄할 문서의 중요도보다 높은 중요도의 문서가 뒤에 대기하고 있는 경우
            printer.append(document) # 다시 대기열의 맨 뒤에 저장
        
    res.append(cnt)

print(*res, sep = '\n')

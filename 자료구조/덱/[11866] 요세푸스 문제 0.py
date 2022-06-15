'''
[11866] 요세푸스 문제 0 / Silver 5 / 자료구조(덱)
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
'''
from collections import deque

N, K = map(int, input().split())
people = deque(str(i) for i in range(1, N+1))

res = []
while True :
    if not people : 
        break
    
    else :
        people.rotate(1-K) # K번째 사람을 deque의 맨 앞에 위치
        res.append(people.popleft()) # 맨 앞의 사람(K번째 사람)을 제거

print('<' + ', '.join(res) + '>')
#print(str(res).replace('[', '<').replace(']', '>'))
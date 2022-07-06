'''
[16466] 콘서트 / Bronze 1 / 자료구조(Set), 구현
HCPC 콘서트의 티켓팅은 매우 치열하며 티켓팅은 2차까지 있다. 이 티켓의 번호가 작을수록 HCPC의 목소리를 가까이에서 들을 수 있다.
양한이는 HCPC 콘서트의 1차 티켓팅을 놓치고, 2차 티켓팅에 도전한다.
양한이는 매우 특별한 정보를 얻었는데, 이는 바로 1차 티켓팅에서 이미 팔린 티켓의 번호들의 목록이다. 티켓의 번호는 1번부터 시작한다.
양한이는 이 목록에 있는 번호들을 가진 티켓을 제외한 티켓 중 번호가 가장 작은 티켓의 번호를 알고 싶다. 양한이를 도와주자!
'''
import sys, heapq
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())) # 1차 티켓팅에서 팔린 티켓의 번호 목록

B = [num for num in range(1, max(A)+2)]

print(min(set(B)-set(A)))

'''
n = int(input())
for index, i in enumerate(sorted(map(int, input().split()))):
    if index + 1 != i:
        print(index + 1)
        break
else:
    print(n + 1)
'''
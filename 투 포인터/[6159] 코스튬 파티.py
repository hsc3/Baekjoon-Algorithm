# [6159] 코스튬 파티 / Silver 5 / 투 포인터
'''
한 농부가 할로윈 파티에 그의 소들을 데려가려고한다. 아쉽게도 농부에게는 코스튬이 한벌밖에 없다.
그 코스튬에는 정확하게 사이즈는 S(1 <= S <= 1,000,000)이며, 최대 소 두마리가 들어간다.
농부는 N(2 <= N <= 20,000)마리의 소가 있으며(소의 이름은 편의상 소1.. 소N으로한다), 소i의 사이즈는 (1 <= L_i <= 1,000,000)이다.
만약 소 두마리의 크기 합이 코스튬의 크기 이하인 경우 둘이 코스튬에 들어갈 수 있다.
농부가 코스튬에 얼마나 많은 서로 다른 소의 짝이 들어가는지 구할수있도록 도와주자.
'''
import sys
input = sys.stdin.readline

N, S = map(int, input().split()) # 소의 수, 코스튬의 크기
cow = sorted(list(int(input()) for _ in range(N)), reverse = True) # 소들의 크기 (내림차순 정렬)

answer = 0
left, right = 0, N-1 # 무거운 소, 가벼운 소를 가리키는 포인터

while left < right:
    weight = cow[left] + cow[right]
    if weight <= S: # 소의 무게를 증가시킬수 있는 경우
        # 내림차순 정렬을 했기 때문에, left 포인터가 가리키는 소보다 가벼운 소들은 모두 right가 가리키는 소와 함께 들어갈 수 있다.
        answer += (right-left)
        right -= 1 # 가벼운 소의 포인터를 이동
    else: # 소의 무게를 감소시켜야 하는 경우
        left += 1 # 무거운 소의 포인터를 이동

print(answer)
        
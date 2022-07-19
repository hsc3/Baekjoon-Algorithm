'''
[1940] 주몽 / Silver 4 / 투 포인터, 정렬
갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다. 갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다.
야철대장은 자신이 만들고 있는 재료를 가지고 갑옷을 몇 개나 만들 수 있는지 궁금해졌다.
이러한 궁금증을 풀어 주기 위하여 N(1 ≤ N ≤ 15,000) 개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input()) # 재료의 개수
M = int(input()) # 갑옷을 만드는데 필요한 수
materials = list(map(int, input().split())) # 재료들의 고유 번호
materials.sort() # 재료들의 고유 번호를 오름차순으로 정렬한다.

small, big = 0, N-1
answer = 0
while small < big:
    number = materials[small] + materials[big] # 재료들의 고유 번호 합을 생성
    if number == M: # 고유 번호 합이 M과 같을 경우 -> 해당 재료들은 다시 사용X
        answer += 1
        small += 1
        big -= 1
    elif number < M: # 고유 번호 합이 M보다 작은 경우 -> 작은 쪽의 고유 번호 + 1
        small += 1
    else: # 고유 번호 합이 M보다 큰 경우 -> 큰 쪽의 고유 번호 - 1
        big -= 1

print(answer)
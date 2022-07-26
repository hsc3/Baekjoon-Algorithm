# [13335] 트럭 | Silver 1 | 자료구조(queue)
'''
다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때,
모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성하라.
'''
import sys
input = sys.stdin.readline

N, W, L = map(int, input().split()) # 트럭의 수, 다리 길이, 다리의 최대 하중
trucks = list(map(int, input().split()))

bridge_weight = 0 # 현재 다리의 하중
bridge = []
seconds = 0

while True :
    seconds += 1
    
    for truck in bridge : # 트럭을 앞으로 이동
        truck[1] += 1
    
    for truck in bridge :
        if truck[1] == W + 1 : # 트럭이 다리를 건넌 경우
            bridge.pop(0)
            bridge_weight -= truck[0]

    if trucks and bridge_weight + trucks[0] <= L : # 추가적으로 트럭이 다리에 올라서는 경우
        bridge_weight += trucks[0]
        truck = [trucks.pop(0), 1]
        bridge.append(truck)

    if not trucks and not bridge : # 모든 트럭이 다리를 건넌 경우 
        break    

    # print(seconds, bridge)
print(seconds)

'''
n, bridge_length, weight = map(int, input().split())
truck_weights = list(map(int, input().split()))
cnt, l = 0, 0
arr = [0] * bridge_length
for i in truck_weights:
   while cnt - arr[l] + i > weight:
      arr.append(0)
      cnt -= arr[l]
      l += 1
   arr.append(i)
   cnt += i - arr[l]
   l += 1

print(len(arr))

=============================================================
N, W, L = map(int, input().split()) # 트럭의 수, 다리 길이, 다리의 최대 하중
trucks = list(map(int, input().split()))

bridge = [0 for _ in range(W)]
seconds = 0

while True :
    seconds += 1
    bridge.pop(0)

    if trucks and sum(bridge) + trucks[0] <= L :
        bridge.append(trucks.pop(0))
    else :
        bridge.append(0)

    if sum(bridge) == 0 :
        break

    print(seconds, bridge)

print(seconds)
'''
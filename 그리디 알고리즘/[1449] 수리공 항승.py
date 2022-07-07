'''
[1449] 수리공 항승 / Silver 3 / 그리디
항승이는 길이가 L인 테이프를 무한개 가지고 있다.
항승이는 테이프를 이용해서 물을 막으려고 한다. 항승이는 항상 물을 막을 때, 적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다고 생각한다.
물이 새는 곳의 위치와, 항승이가 가지고 있는 테이프의 길이 L이 주어졌을 때, 항승이가 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하시오.
테이프를 자를 수 없고, 테이프를 겹쳐서 붙이는 것도 가능하다.
'''
import sys
input = sys.stdin.readline

N, L = map(int, input().split()) 
location = sorted(list(map(int, input().split())))

tape = L-1 # 테이프가 커버할 수 있는 간격
res = 1

for i in range(len(location)-1) :
    if location[i+1] - location[i] <= tape : # 다음 위치(location[i+1])까지 커버할 수 있는 경우
        tape -= (location[i+1]-location[i])
    else : # 커버할 수 없는 경우, 새로운 테이프 사용
        tape = L-1
        res += 1

print(res)

'''
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
location = sorted(list(map(int, input().split())))

cursor = 0 # 위치를 가리키는 커서 (0 ~ 마지막으로 물이 새는 곳)
res = 0

while cursor <= location[-1] :
    if cursor in location : # 해당 위치가 물이 새는 곳인 경우, 길이 L의 테이프를 붙인다. (해당 위치+L 의 지점부터 다시 점검)
        cursor += L
        res += 1
    else :
        cursor += 1

print(res)
'''
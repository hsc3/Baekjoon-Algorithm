'''
[6603] 로또 | Silver 2 | 백트랙킹
독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.
로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.
각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.
'''
import sys
input = sys.stdin.readline

def BackTracking(choose, prev) :
    if len(choose) == 6 :
        print(*choose)
        return

    for i in range(prev+1, l[0]+1) :
        BackTracking(choose + [l[i]], i)

if __name__ == "__main__":
    while True :
        l = list(map(int, input().split()))
        if not l[0] : break
        BackTracking([], 0)
        print()
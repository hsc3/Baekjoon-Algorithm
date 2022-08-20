'''
[15649] N과 M (1) | Silver 3 | 백트랙킹
자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 모두 구하는 프로그램을 작성하시오.
중복되는 수열을 여러 번 출력하면 안되며, 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
Backtracking :  모든 가능한 경우의 수 중에서 특정한 조건을 만족하는 경우만 살펴보는 것
'''
# 이미 고른 숫자인지, 총 몇 개 골랐는지
import sys
input = sys.stdin.readline

def Select(n, m, choose, visited) :
    if m == 0 : # m개의 숫자를 골랐으면 종료
        print(*choose)
        return
    for num in range(1, n+1) :
        if visited[num] == False : # 아직 선택하지 않은 숫자인 경우
            choose.append(num)
            visited[num] = True
            Select(n, m-1, choose, visited) # num을 선택하고 다음 숫자를 선택하러 넘아감
            choose.remove(num)
            visited[num] = False # num을 선택하지 않고 다음 숫자를 선택하러 넘어감

if __name__ == "__main__":
    n, m = map(int, input().split())
    visited = [False for _ in range(n+1)]
    Select(n, m, [], visited)
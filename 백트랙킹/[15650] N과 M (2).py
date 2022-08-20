'''
[15650] N과 M (2) | Silver 3 | 백트랙킹
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열, 고른 수열은 오름차순이어야 한다.
'''
import sys
input = sys.stdin.readline

def Select(choose, visited, i, prev) :
    if i == m : # m개의 숫자를 모두 선택한 경우 출력
        print(*choose)
        return
    for num in range(1, n+1) :
        if visited[num] == False and prev < num : # 아직 고르지 않은 숫자이고 이전 숫자보다 큰 경우

            visited[num] = True # (여기서 선택을 하지 않으면 다시는 선택할 수 없음)
            Select(choose + [num], visited, i+1, num) # num을 선택하고 다음 숫자를 선택하러 이동
            visited[num] = False # num을 선택하지 않고 다음 숫자로 이동

if __name__ == "__main__":
    n, m = map(int, input().split())
    visited = [False for _ in range(n+1)]
    Select([], visited, 0, 0)
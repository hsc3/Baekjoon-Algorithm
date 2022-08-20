'''
[15652] N과 M (4) | Silver 3 | 백트랙킹
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 M개를 고른 수열, 같은 수를 여러 번 골라도 된다, 고른 수열은 비내림차순이어야 한다.
(길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.)
'''
import sys
input = sys.stdin.readline

def Select(choose, cnt, prev) :
    if cnt == m :
        print(' '.join(choose))
        return
    for num in range(1, n+1) :
        if prev <= num :
            # num을 선택하고 다음으로 넘어가는 경우와, num을 선택하지 않고 넘어가는 경우로 갈라진다.
            Select(choose + str(num), cnt+1, num)

if __name__ == "__main__":
    n, m = map(int, input().split())
    choose = ""
    Select(choose, 0, 1)
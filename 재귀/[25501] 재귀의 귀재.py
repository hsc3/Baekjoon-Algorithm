# [25501] 재귀의 귀재 | Bronze 2 | 재귀
'''
팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다.
어떤 문자열이 팰린드롬인지 판별하는 문제는 재귀 함수를 이용해 쉽게 해결할 수 있다. isPalindrome 함수는 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환하는 함수다.
정휘는 isPalindrome 함수를 이용하여 어떤 문자열이 팰린드롬인지 여부를 판단하려고 한다. 정휘를 따라 여러분도 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.
'''
import sys
input = sys.stdin.readline

def isPalindrom(str, l, r, cnt):
    if l >= r:
        return [1, cnt]
    elif str[l] != str[r]:
        return [0, cnt]

    return isPalindrom(str, l+1, r-1, cnt+1)

if __name__ == "__main__":
    answer = []
    T = int(input())
    for _ in range(T):
        str = input().rstrip()
        answer.append(isPalindrom(str, 0, len(str)-1, 1))

    for i in range(T):
        print(*answer[i])


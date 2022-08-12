'''
[14425] 문자열 집합 | Silver 3 | 자료구조 (Map)
총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def HashFunc(str) :
    n = 0
    for c in str:
        n += ord(c)
    return n

if __name__ == "__main__":
    N, M = map(int, input().split())
    S = dict()
    for _ in range(N) :
        str = input()
        str_h = HashFunc(str) # 문자열을 해시함수로 변환
        S[str_h] = S.get(str_h, []) + [str]

    cnt = 0
    for _ in range(M) :
        str = input()
        str_h = HashFunc(str)
        if str_h in S.keys() :
            if str in S[str_h] :
                cnt += 1 # 집합 S에 포함되어 있는 경우
    print(cnt)

# 해싱하지 않고, 그냥 문자열 자체를 dict의 key값으로 저장하는게 더 빠르다.

# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# S = {}
# for _ in range(N) :
#     str = input()
#     S[str] = S.get(str, 0) + 1
#
# cnt = 0
# for _ in range(M) :
#     str = input()
#     if str in S.keys() :
#         cnt += 1
#
# print(cnt)
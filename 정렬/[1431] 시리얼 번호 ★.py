# [1431] 시리얼 번호 | Silver 3 | 정렬 
'''
A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
'''
from functools import cmp_to_key
import sys
input = sys.stdin.readline
def SNsort(s1, s2) :
    if len(s1) > len(s2) : 
        return 1
    elif len(s1) == len(s2) :
        sum_of_s1 = 0
        sum_of_s2 = 0
        for i in range(len(s1)) :
            if s1[i].isnumeric() :
                sum_of_s1 += int(s1[i])
            if s2[i].isnumeric() :
                sum_of_s2 += int(s2[i])
        if sum_of_s1 > sum_of_s2 :
            return 1
        elif sum_of_s1 == sum_of_s2 :
            if s1 > s2 : # 사전순 비교는 문자열의 한자리씩 할 필요가 없다 !!!
                return 1
    return -1


N = int(input())
guitar = []
for _ in range(N) :
    guitar.append(input().rstrip())
guitar.sort(key = cmp_to_key(SNsort))
print(*guitar, sep='\n')

'''
import sys
n = int(sys.stdin.readline())
code = [sys.stdin.readline()[:-1] for _ in range(n)] # 문자열 마지막의 개행 생략
code = sorted(code, key=lambda x: (len(x), sum([int(i) for i in x if i.isnumeric()]), x))
print("\n".join(code))
'''
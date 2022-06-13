# 알고리즘 : 구현, 문자열
# [1259] 펠린드롬 수 
# https://www.acmicpc.net/problem/1259

import sys
input = sys.stdin.readline

def IsFelindrom(number) :
    start = 0
    end = len(number)-1
    while start < end : 
        if number[start] != number[end] :
            return False
        else :
            start += 1
            end -= 1
    return True

def Solution() :
    ans = []
    while True :
        data = int(input())
        if data == 0 : 
            break
        
        if IsFelindrom(str(data)) :
            ans.append("yes")
        else : 
            ans.append("no")

    print(*ans, sep='\n')

if __name__=="__main__" :
    Solution()

'''
- 다른 풀이법 -

(1) if n == n[::-1]

(2) if string_n == ''.join(reversed(string_n)):

'''


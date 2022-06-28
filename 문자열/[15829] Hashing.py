'''
[15829] Hashing / Bronze 2 / 문자열
해시 함수란 임의의 길이의 입력을 받아서 고정된 길이의 출력을 내보내는 함수로 정의한다. 대표적으로 자료의 저장과 탐색에 쓰인다.
먼저, 편의상 입력으로 들어오는 문자열에는 영문 소문자(a, b, ..., z)로만 구성되어있다고 가정하자.
영어에는 총 26개의 알파벳이 존재하므로 a에는 1, b에는 2, c에는 3, ..., z에는 26으로 고유한 번호를 부여할 수 있다.
결과적으로 우리는 하나의 문자열을 수열로 변환할 수 있다. 예를 들어서 문자열 "abba"은 수열 1, 2, 2, 1로 나타낼 수 있다.

간단하게는 수열의 값을 모두 더할 수도 있다. 해시 함수의 정의에서 유한한 범위의 출력을 가져야 한다고 했으니까 적당히 큰 수 M으로 나눠주자.
항의 번호에 해당하는 만큼 특정한 숫자를 거듭제곱해서 곱해준 다음 더하는 것이 있다.
r의 값은 26보다 큰 소수인 31로 하고 M의 값은 1234567891(놀랍게도 소수이다!!)로 하자.
문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력하자.
'''

import sys
input = sys.stdin.readline

L = int(input())
stringData = input().rstrip()

# 입력받은 문자열을 고유한 번호로 변환. (a의 아스키코드는 97)
stringToNumber = [ord(s)-96 for s in stringData]

res = 0
for i in range(len(stringToNumber)) :
    res += ((stringToNumber[i] * (31**i)))

print(res % 1234567891)

'''
import sys

l = int(sys.stdin.readline())
hash_str = str(sys.stdin.readline())
sum = 0
for i in range(l):

    char = hash_str[i]
    sum = sum + (ord(char)-96)*(31**i)
    
hash = sum % 1234567891
print(sum)
'''

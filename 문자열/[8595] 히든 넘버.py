# [8595] 히든 넘버 / Bronze 1 / 문자열
'''
단어에 숫자가 숨어있다. 이 숫자를 히든 넘버라고 한다. 알파벳 대/소문자와 숫자로 이루어진 단어가 주어졌을 때, 모든 히든 넘버의 합을 구하는 프로그램을 작성하시오.
단어와 히든 넘버는 아래와 같은 성질을 갖는다.
- 연속된 숫자는 한 히든 넘버이다.
- 두 히든 넘버 사이에는 글자가 적어도 한 개 있다.
- 히든 넘버는 6자리를 넘지 않는다.
'''
import sys
input = sys.stdin.readline

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']

n = int(input())
str = input().lower().rstrip() # 문자열의 알파벳을 모두 소문자로 변경

for a in alpha: # 단어의 모든 알파벳을 ' '로 변경
    str = str.replace(a, ' ')

numbers = list(map(int, str.split())) # ' ' 기준으로 문자열을 파싱
print(sum(numbers))

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# str = list(input().rstrip())
#
# answer = 0
# number = []
# for i in range(n+1):
#     if i == n or str[i].isalpha(): # 알파벳인 경우 → 이전에 등장한 히든 넘버를 저장한다.
#         if 0 < len(number) <= 6:
#             answer += (int(''.join(number)))
#         number.clear()
#     else: # 숫자인 경우 → number 문자열에 숫자를 저장한다.
#         number.append(str[i])
#
# print(answer)
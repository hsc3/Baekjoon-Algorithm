# [1213] 팰린드롬 만들기 | Silver 3 | 문자열
'''
임한수와 임문빈은 서로 사랑하는 사이이다. 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.
임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.
임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.
만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.
'''
import sys
from collections import Counter
input = sys.stdin.readline

name = input().rstrip()
word = Counter(name)

left, mid = '', ''   # 팰린드롬 문자열의 왼쪽 문자열과 가운데 문자열 (왼쪽 문자열은 오른쪽 문자열과 대칭)

for key in sorted(word.keys()): # 사전 순으로 빠른 팰린드롬 문자열을 만듭니다.
    left += key * (word[key] // 2) # 문자의 절반은 왼쪽 문자열에 넣습니다.
    mid += key * (word[key] % 2) # 남은 문자는 중간 문자열에 넣습니다.

palindrom = left + mid + left[::-1]
print(palindrom if palindrom == palindrom[::-1] else "I'm Sorry Hansoo")
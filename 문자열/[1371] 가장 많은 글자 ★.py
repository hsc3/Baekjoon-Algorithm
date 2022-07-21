'''
[1371] 가장 많은 글자 / Bronze 1 / 문자열
영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.
어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.
'''
import sys
inputText = sys.stdin.read()
# read() : 파일 전체의 내용을 하나의 문자열로 읽어온다.
# readline() : 한번에 하나의 라인을 읽어오는 메소드이다.

counter = dict()
for ch in inputText:
    if ch != ' ' and ch != '\n':
        counter[ch] = counter.get(ch, 0) + 1

counter = sorted(counter.items(), key = lambda x : -x[1])
maxValue = counter[0][1] # 제일 많은 문자의 수

answer = []
for key, value in counter:
    if value == maxValue:
        answer.append(key)

print(*sorted(answer), sep = '')

# from collections import Counter
#
# counter = Counter()
# while True:
#     try:
#         words = list(input().rsplit())
#         for word in words:
#             counter.update(Counter(word)) # 결과를 기존 counter와 누적
#     except EOFError: 
#         break
#
# answer = []
# maxValue = max(counter.values())
# for key, value in counter.most_common(): # 문자의 수 기준 내림차순 정렬을 얻을 수 있음
#     if value == maxValue:
#         answer.append(key)
#     else:
#         break
#
# print(*sorted(answer), sep = '')